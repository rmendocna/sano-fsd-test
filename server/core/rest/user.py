# API for user authenticated endpoints
# Note: none of these endpoints should have a user_id or user_email parameter passed in via the request.
# the user_id and user_email is obtained from the JWT, if valid
import io
import json
import logging
from datetime import datetime as dt

import numpy as np
import pytz
import shortuuid
from flask import abort
from flask import Blueprint
from flask import current_app as app
from flask import jsonify, request
from flask_cors import CORS
from peewee import IntegrityError, DoesNotExist
from playhouse.shortcuts import model_to_dict

from core.auth.decorators import user_only
from core.models import Enrollments, Studies, Users

tz = pytz.timezone("Europe/London")
user_api = Blueprint("user_api", __name__)
logger = logging.getLogger(__name__)

CORS(user_api, supports_credentials=True)


# An example user authenticated endpoint.
@user_api.route("/user", methods=["GET"])
@user_only
def get_user(user_id, user_email):
    return jsonify(user_id)


@user_api.route("/enrol/delete/<study_id>", methods=["DELETE"])
@user_only
def delete_enrollment(user_id, user_email, study_id):
    study = Studies.get_by_id(study_id)
    user = Users.get_by_id(user_id)
    try:
        enroll = Enrollments.get(Enrollments.study == study, Enrollments.user == user)
    except DoesNotExist:
        return {"error": 'Could not find the given enrollment'}, 404
    except Exception as e:
        return {"error": '%s' % e}, 500
    else:
        enroll.delete()
        d = model_to_dict(study)
        d.update({'enrolled': False})
        return d


@user_api.route("/enrol/create", methods=["POST"])
@user_only
def create_enrollment(user_id, user_email):
    data = request.get_json()
    study_id = data['study_id']
    study = Studies.get_by_id(study_id)
    user = Users.get(Users.email == user_email)
    enroll = Enrollments(study=study, user=user)
    try:
        enroll.save(force_insert=True)
    except IntegrityError as e:
        return jsonify({"error": "%s" % e}), 500
    d = model_to_dict(study)
    d.update({'enrolled': True})
    return d


@user_api.route("/enrollments", methods=["GET"])
@user_only
def get_enrollments(user_id, user_email):
    user = Users.get(Users.email == user_email)
    enrollments = Enrollments.select(Enrollments.study_id).filter(Enrollments.user == user).tuples()
    return jsonify([e[0] for e in enrollments])



