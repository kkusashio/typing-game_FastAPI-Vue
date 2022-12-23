<template>
  <v-app>
    <v-main>
      <h1 class="display-2 font-weight-black ml-10 mt-10">
        Welcome to Vuetify 3 Beta
      </h1>
      <v-container>
        <v-row class="ma-8">
          <v-col v-for="[title] in links"  :key="title" cols="4">
            <v-card height="150" class="ma-8" @click="toType">
              <v-card-title class="text-center">{{title}}</v-card-title>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
  <TypingApp></TypingApp>
</template>

<script lang="ts">
import TypingApp from '../components/TypingApp.vue'
import { useRouter } from 'vue-router'
const router = useRouter();
console.log(router)
export default {
  name: "HomeView",
  data(){
    return{
      links: [
        ['TOEIC 900'],
        ['TOEIC 600'],
        ['YAKOHLAB SPECIAL']
      ],
   }
  },
  components: {
    TypingApp
  },
  methods: {
    toType: function () {
      router.push("/user")
    }
  }
};
</script>

<style>
</style>