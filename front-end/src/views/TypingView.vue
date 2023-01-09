<template>
  <v-app class="typing-bg">
    <v-main>
      <h1 class="center">{{ words }}</h1>
      <!-- <h1 class="center">{{ level }}</h1> -->
      <TypingApp v-bind:level="level"></TypingApp>
    </v-main>
  </v-app>
</template>

<script>
import TypingApp from "../components/TypingApp.vue";
export default {
  name: "TypingView",
  components: {
    TypingApp,
  },
  data() {
    return {
      words: "",
      level: 0,
    };
  },
  created() {
    this.words = this.$route.query.words;
    this.level = this.$route.query.level;
  },
};
</script>

<style>
.center {
  text-align: center;
  margin-top: 20px;
}
.typing-bg {
  background-color: #fafafa;
}
</style>
