<template>
  <v-app>
    <div id="list-demo">
      <button v-on:click="add">Add</button>
      <button v-on:click="remove">Remove</button>
      <transition-group name="list" tag="p">
        <span v-for="item in items" v-bind:key="item" class="list-item">
          {{ item }}
        </span>
      </transition-group>
    </div>
    <transition-group name="animation" tag="animation" v-if="display" >
      <li v-for="todo in links" v-bind:key="todo.id">
        {{ todo.name }}
      </li>
    </transition-group>  

    <div>
      <transition name="animation">
        <h1 style="margin-top:30px" v-if="display">表示箇所</h1>
      </transition>
    </div>

  </v-app>
  
</template>
<script>

export default {
  data() {
    return {
      display: false,
      items: [],
      links: [
        { id: 1, name: 'item01', show: true },
        { id: 2, name: 'item02', show: true },
        // { id: 3, name: 'item03', show: true },
        // { id: 4, name: 'item04', show: true },
        // { id: 5, name: 'item05', show: true },
        // { id: 6, name: 'item06', show: true },
        // { id: 7, name: 'item07', show: true },
        // { id: 8, name: 'item08', show: true },
        // { id: 9, name: 'item09', show: true }
      ],
    }
  },
  mounted() {
    this.changeDisplay()
  },
  methods: {
    changeDisplay: function() {
      this.display = true
      this.items=[1,2,3,4,5,6,7,8,9]
    },
    randomIndex: function () {
      return Math.floor(Math.random() * this.items.length)
    },
    add: function () {
      this.items.splice(this.randomIndex(), 0, this.nextNum++)
    },
    remove: function () {
      this.items.splice(this.randomIndex(), 1)
    },
  }
}
</script>
<style scoped>
/* .animation-enter {
  opacity: 0;
} */

.animation-enter-active {
  animation: slide 1s;
  transition: opacity 1s;
}

/* .animation-enter-to {
  opacity: 1;
} */

/* .animation-leave {
  opacity: 1;
}

.animation-leave-active {
  animation: slide 1s reverse;
  transition: opacity 3s;
}

.animation-leave-to {
  opacity: 0;
} */

@keyframes slide {
  from {
    transform: translateY(200px);
    opacity: 0;
  }

  to {
    transform: translateX(0);
    opacity: 1;
  }
}
.list-item {
  display: inline-block;
  margin-right: 10px;
}

.list-enter-active,
.list-leave-active {
  transition: all 1s;
}

.list-enter,
.list-leave-to

/* .list-leave-active for below version 2.1.8 */
  {
  opacity: 0;
  transform: translateY(60px);
}
</style>