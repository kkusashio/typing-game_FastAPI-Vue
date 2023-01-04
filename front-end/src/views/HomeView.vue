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
</template>

<script>
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
  methods: {
    toType: function () {
      // https://qiita.com/Engineer_Grotle/items/66d181309a779ce8a34a
      this.$router.push({ name: "typing", query: { words: "TOEIC900"} })
    }
  }
};
</script>

<style>
</style>