<template>
    <v-app>
        <h1 class="center">{{ words }}</h1>
        <TypingApp></TypingApp>

    </v-app>
    
</template>

<script>
import TypingApp from '../components/TypingApp.vue'
export default {
    name: "TypingView",
    components: {
        TypingApp
    },
    data() {
        return {
            words: '',
        }
    },
    created() {
        this.words=this.$route.query.words
    }
};
</script>

<style>
.center {
    text-align: center;
    margin-top: 20px;
}
</style>