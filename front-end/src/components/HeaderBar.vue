<template>
  <div>
      <v-app-bar 
      color="surface" 
      height="100" 
      class="el" 
      app 
      :style="{ padding : $vuetify.breakpoint.mdAndUp ? '0px 100px': '' }"
      >
      <v-toolbar-title 
      @click="$router.push('/')" 
      class="text-md-h5 font-weight-bold pointer">
      <img src="/logo.png"  width="100vh">
      </v-toolbar-title>
      
      <v-spacer/>
      <v-btn nuxt to="/projects" icon>
          <v-icon size="20">mdi-application-brackets</v-icon>
      </v-btn>
      <v-btn nuxt to="/members" icon>
          <v-icon size="20">mdi-account-group</v-icon>
      </v-btn>
      <v-divider vertical class="mx-md-5 mx-2"/>
      <v-btn nuxt to="/" icon>
          <v-icon size="20">mdi-home</v-icon>
      </v-btn>
      </v-app-bar>
  </div>
</template>