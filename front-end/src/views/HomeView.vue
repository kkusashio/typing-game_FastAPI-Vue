<template>
  <v-app>
    <!-- <v-parallax :src="require('@/assets/newspaper_blur.jpg')"> -->
    <v-main class="bg">
      <h1 class="display-2 font-weight-black ml-10 mt-10 center">SELECT</h1>
      <v-container>
        <v-row class="ma-8">
          <transition-group name="list">
            <v-col
              v-for="item in links"
              :key="item"
              class="list-item"
              :style="{ 'transition-delay': `${item.id * 0.3}s` }"
              cols="4"
            >
              <v-card height="150" class="ma-8" @click="toType" color="">
                <v-card-title class="text-center inner-center">{{
                  item.name
                }}</v-card-title>
              </v-card>
            </v-col>
          </transition-group>
        </v-row>
      </v-container>
    </v-main>
    <!-- </v-parallax> -->
  </v-app>
</template>

<script>
export default {
  name: "HomeView",
  data() {
    return {
      links: [],
    };
  },
  methods: {
    toType: function () {
      // https://qiita.com/Engineer_Grotle/items/66d181309a779ce8a34a
      this.$router.push({
        name: "typing",
        query: { words: "TOEIC900", level: 5 },
      });
    },
  },
  mounted() {
    this.links = [
      { id: 1, name: "TOEIC900" ,level:5},
      { id: 2, name: "TOEIC700" },
      { id: 3, name: "TOEIC500" },
      { id: 4, name: "TOEIC300" },
      { id: 5, name: "TOEIC100" },
    ];
  },
};
</script>

<style scoped>
.center {
  text-align: center;
}
.inner-center {
  margin-top: 50px;
}
.bg {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  background-size: cover;
  background-color: #fafafa;
}

.list-enter-active {
  transition: all 1s ease-out;
}

.list-enter-to {
  opacity: 1s;
  transform: translateY(0px);
}

.list-enter-from {
  opacity: 0;
  transform: translateY(300px);
}
</style>
