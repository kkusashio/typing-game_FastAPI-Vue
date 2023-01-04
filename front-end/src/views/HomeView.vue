<template>
  <v-app>
    <v-parallax :src="require('@/assets/newspaper_blur.jpg')">
    <v-main class="">
      <h1 class="display-2 font-weight-black ml-10 mt-10 center">
        Let's Typing
      </h1>
      <v-container>
        <v-row class="ma-8">
          <v-col v-for="[title] in links"  :key="title" cols="4">
            <v-card height="150" class="ma-8" @click="toType">
              <v-card-title class="text-center inner-center">{{title}}</v-card-title>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
    </v-parallax>

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

<style scoped>
.center{
  text-align:center;
}
.inner-center{
  margin-top: 50px;
}
.bg {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  background-size: cover;
  background-image: url("~@/assets/newspaper.jpg");
}
</style>