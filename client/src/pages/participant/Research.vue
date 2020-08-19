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
                            <div v-for="std in studies" class="flex xs:flex-col md:flex-row w-full border border-sano-pink p-3">
                                <div class="xs:w-full md:w-1/4 flex md:flex-col-reverse xs:flex-row-reverse xs:justify-between items-start md:border-l md:border-sano-pink pl-3">
                                    <div :class="{'text-white text-center uppercase rounded-full text-sm mt-3 p-3 pt-1 pb-1': true, 'bg-sano-blue': std.visible, 'bg-sano-green': !std.visible}">
                                        <small v-if="std.visible">Complete</small>
                                        <small v-else>In Progress</small>
                                    </div>
                                    <div v-if="!std.visible" class="text-sano-red-orange">ENROLLED</div>
                                </div>
                                <div class="xs:w-full md:w-1/2 md:order-first">
                                    <h1>{{ std.title }}</h1>
                                    <small class="text-xs text-grey">Run by Sano Genetics</small>
                                </div>
                                <div class="xs:w-full md:w-1/4 md:border-l md:border-sano-pink pl-3 flex flex-col-reverse">
                                    <button v-if="!std.visible" class="leave sano-btn sano-btn-narrow">Leave study</button>
                                    <button v-else class="join sano-btn sano-btn-narrow">Join study</button>
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

export default {
    name: "Research",
    components: {
        LoggedinSidebarTemplate,
    },
    data () {
        return {studies: []}
    },
    mounted () {
        let self = this;
        self.$http.get('/api/research').then((resp) => {
            self.studies = resp.data
        }).catch((error) => { alert('Could not get studies') })
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
