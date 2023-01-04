<template>
    <div>
      <v-card tile flat class="pa-md-10 pa-5 text-center" color="surface">
        <h2 class="text-md-h6 font-weight-bold">Contact Us</h2>
        <br />
        <div class="text-center">
          <v-btn v-for="(b,i) in sm" :key="`socialMedia-${i}`" color="surface" class="mr-2" fab depressed :href="`${b.link}`" target="_blank" rel="noopener noreferrer">
            <v-icon >{{b.icon}}</v-icon>
          </v-btn>
        </div>
      </v-card>
    </div>
</template>

<script lang="ts">
export default {
  data(){
    return{
      sm:[
        {
          icon:"mdi-twitter",
          link:'https://twitter.com/aicebreak',
        },
        {
          icon:"mdi-gmail",
          link:'mailto:aicebreak.co@gmail.com',
        },
      ]
    }
  }
};
</script>

<style></style>