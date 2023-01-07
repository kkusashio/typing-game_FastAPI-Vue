<template >
  <v-app>
      <v-main class="bg">

        <v-container>
          <v-row class="ma-8">
            <transition-group name="list">
              <v-col v-for="(item) in links" :key="item" class="list-item"
                :style="{ 'transition-delay': `${item.id * 0.3}s` }" cols="4">
                <v-card height="150" class="ma-8" >
                  <v-card-title class="text-center">{{ item.name }}</v-card-title>
                </v-card>
              </v-col>
            </transition-group>
          </v-row>
        </v-container>
      </v-main>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      links: [
      ],
    }
  },
  methods: {
    
  },
  mounted() {
    this.links = [
      { id: 1, name: "Page1" },
      { id: 2, name: "Page2" },
      { id: 3, name: "Page3" },
      { id: 4, name: "Page4" },
      { id: 5, name: "Page5" },
    ]
  }
};
</script>

<style scoped>


.bg {
  background-color: rgb(222, 212, 199);
  /* background-image: url("~@/assets/newspaper.jpg"); */
}


.list-enter-active {
  transition: all 1s ease-out;
}


.list-enter-to {
  opacity: 1.0s;
  transform: translateY(0px);
}

.list-enter-from {
  opacity: 0;
  transform: translateY(300px);
}
</style>