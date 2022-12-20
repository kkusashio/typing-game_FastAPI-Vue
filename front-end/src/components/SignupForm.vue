<!-- https://qiita.com/sand/items/4b3e222dbb9315e2b0c0#3-vue%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0 -->
<template>
    <v-app>
        <v-card width="400" class="mx-auto mt-5">
            <v-card-title class="text-center">{{ title }}</v-card-title>
            <v-form style="width:380px">
                <v-text-field variant="outlined" density="comfortable" prepend-icon="mdi-account-circle"
                    label="username" v-model="username" />
                <v-text-field variant="outlined" density="comfortable" prepend-icon="mdi-email" 
                    label="mail-address" v-model="email" />
                <v-text-field v-bind:type="showPassword ? 'text' : 'password'" variant="outlined" density="comfortable"
                    prepend-icon="mdi-lock" v-bind:append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                    label="password" @click:append="showPassword = !showPassword" v-model="password" />
                <v-text-field v-bind:type="showPassword ? 'text' : 'password'" variant="outlined" density="comfortable"
                    prepend-icon="mdi-lock" v-bind:append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'" label="confirm password"
                    @click:append="showPassword = !showPassword" v-model="password2" />
                <v-card-actions class="justify-center">
                    <v-btn variant="outlined" @click="doSignup">Signup</v-btn>
                </v-card-actions>
                <p class="text-center" color="red">{{ errormessage }}</p>
            </v-form>
            <!-- <p>Current token = {{ token }}</p> -->
        </v-card>
    </v-app>
</template>

<script>
// import { inject } from 'vue'
import axios from 'axios'

export default {
    data() {
        return {
            title: "Signup",
            token: "",
            showPassword: false,
            username: "",
            password: "",
            password2: "",
            email:"",
            errormessage:"",
        }
    },
    methods: {
        doSignup: function () {
            console.log("doSignup:: username=", this.username, " passowrd=", this.password,"email=",this.email)

            const params = {
                "email": this.email,
                "username": this.username,
                "password": this.password
            }
            if (this.password === this.password2) {
                let config = {
                    headers: {
                        'Content-Type': 'application/json'
                    }
                };
                const URL = 'http://localhost:8000/users/'
                console.log("aaaaaa")
                axios.post(URL, params, config)
                    .then((response) => {
                        console.log("response.data = ", response.data)
                        this.token = response.data.access_token
                        localStorage.setItem('token', response.data.access_token);
                        this.$emit('change-login', true)
                        this.$router.push({
                            name: 'home',
                        })
                    })
                    .catch((err) => {
                        console.log("Error = ", err)
                    })
                
            } else { 
                this.errormessage = "not match"
            }
            
        }
    }

}
</script>

<style scoped>

</style>