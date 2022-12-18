<template>
    <v-card width="200" class="mx-auto mt-5">
        <v-card-actions class="justify-center">
            <v-btn to="/" @click="doLogout">Logout</v-btn>
        </v-card-actions>
        
    </v-card>

</template>
<script>
export default {
    data() { 
        return {
            //
        }
    },
    methods: {
        doLogout: function () { 
            localStorage.setItem('token', '');
            this.$emit('change-login',false)
        }
    }
}
</script>