<template>
    <LoggedinSidebarTemplate page_name="research">
        <template v-slot:main-content>
            <div class="max-w-xl mx-auto mb-10 sm:mb-0 min-h-screen">
                <div class="max-w-xl mx-auto lg:px-4">
                <div id="explanation" ref="explanation" class="relative w-full" tabindex="-1" style="top: -4.2rem;"></div>

                    <section id="core-data" class="sect">
                        <div class="flex items-center w-full mb-2">
                            <!-- eslint-disable-next-line max-len --><!-- prettier-ignore -->
                            <div class="sano-border-shine sano-border-shine-orange bg-white w-7 h-7 rounded mr-3 flex flex-col justify-center items-center">
                                <svg class="pl-px w-5 h-3 relative sano-svg-red-orange z-10">
                                    <use xlink:href="#sano-symbol" />
                                </svg>
                            </div>
                            <h2 class="text-sano-burgundy text-xl">
                                My Studies
                            </h2>
                        </div>
                        <div class="flex-col">
                            <div class="md:flex w-full text-gray text-sm uppercase xs:hidden mb-3">
                                <div class="w-1/2">
                                    <small>Study</small>
                                </div>
                                <div class="w-1/4">
                                    <small>Status</small>
                                </div>
                                <div class="w-1/4">
                                    <small>Actions</small>
                                </div>
                            </div>
                            <div v-for="std in studies_enrolls" class="flex xs:flex-col md:flex-row w-full border border-sano-pink p-3">
                                <div class="xs:w-full md:w-1/4 flex md:flex-col-reverse xs:flex-row-reverse xs:justify-between items-start md:border-l md:border-sano-pink pl-3">
                                    <div :class="{'text-white text-center uppercase rounded-full text-sm mt-3 p-3 pt-1 pb-1': true, 'bg-sano-blue': !std.enrolled, 'bg-sano-green': std.enrolled}">
                                        <small v-if="!std.enrolled">Complete</small>
                                        <small v-else>In Progress</small>
                                    </div>
                                    <div v-if="std.enrolled" class="text-sano-red-orange">ENROLLED</div>
                                </div>
                                <div class="xs:w-full md:w-1/2 md:order-first">
                                    <h1>{{ std.title }}</h1>
                                    <small class="text-xs text-grey">Run by Sano Genetics</small>
                                </div>
                                <div class="xs:w-full md:w-1/4 md:border-l md:border-sano-pink pl-3 flex flex-col-reverse">
                                    <button v-if="std.enrolled" @click="delete_enrollment(std.id)" class="leave sano-btn sano-btn-narrow">Leave study</button>
                                    <button v-else @click="create_enrollment(std.id)" class="join sano-btn sano-btn-narrow">Join study</button>
                                </div>
                            </div>
                        </div>
                    </section>
                </div>
                </div>
            </div>
        </template>
        <template v-slot:sidebar-content>
        </template>
    </LoggedinSidebarTemplate>
</template>

<script>

import LoggedinSidebarTemplate from "@/layouts/LoggedinSidebarTemplate";
// import get_studies from "@/api/server/public"
import { each, find } from "lodash";


export default {
    name: "Research",
    components: {
        LoggedinSidebarTemplate,
    },
    data () {
        return {
            studies: [],
            enrollments: []
            }
    },
    methods: {
        delete_enrollment (study_id) {
            let self = this;
            self.$http.delete(`/enrol/delete/${study_id}`,
                              {withCredentials: true}
                       ).then((resp) => {
                            let i = self.enrollments.indexOf(study_id)
                            self.enrollments.splice(i, 1)
                       })
        },
        create_enrollment (study_id) {
            let self = this;
            self.$http.post('/enrol/create',
                            {study_id:study_id},
                            // {withCredentials: true}
                       ).then((resp) => {
                            self.enrollments.push(study_id)
                       }).catch((error) => {
                            alert('Could not enroll')
                       })
        }
    },
    computed: {
        studies_enrolls () {
            let self = this
            let stds = self.studies.slice()
            stds.forEach(function (s) {
                 s.enrolled = self.enrollments.indexOf(s.id) >= 0
             })
            return stds
        }
    },
    mounted () {
        let self = this;
        self.$http.get('/api/studies').then((resp) => {
           self.studies = resp.data
        }).catch((error) => { alert('Could not get studies') })
        self.$http.get('/enrollments', {}, {withCredentials: true}).then((resp) => {
           self.enrollments = resp.data
        }).catch((error) => { alert('Could not get enrollments') })
    }
};
</script>

<style scoped lang="scss">
.mobile-sticky {
    top: 1rem;
}
.sect {
    @apply relative mt-6 mx-4 px-4 py-6 border border-sano-pink rounded overflow-hidden bg-white;
    @media (min-width: 992px) {
        @apply p-8 mx-0;
    }
}

.leave {
    @apply bg-sano-pink border-sano-pink text-sm text-sano-burgundy pt-1 pb-1
}
.join {
    @apply bg-sano-red-orange text-white text-sm text-sano-burgundy pt-1 pb-1
}

@media (max-width: 575px) {
    .mobile-sticky {
        @apply sticky bg-white -ml-4 px-4 border-b border-sano-pink;
        z-index: 99;
        top: 0;
        width: calc(100% + 2rem);
    }

    .sano-toggle-label.sano-toggle-label {
        padding: 0 0.75rem;
    }
}
</style>
