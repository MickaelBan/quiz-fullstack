
<template>

    <div id="login" v-if="isToken">

        <label for="login">Mot de passe </label>
        <input type="password" v-model="pwd"/>
        <div class="button">
            <input type="submit" name="login" value="Connexion" v-on:click="login(pwd)">
        </div>
    </div>

    <div id="back-office" v-else>
        <p>Bien joué bg</p>
    </div>

</template>

<style>
</style>

<script>
import QuizApiService from "../services/QuizApiService";



export default {
    name: "Login",

    data(){
        let adminMode = false;
        return(adminMode);
    },
    methods: {
        login(pwd){
            let response = QuizApiService.postLogin(pwd)
            console.log(response)
        }
    },
    computed: {
        isToken(){
            let token = window.localStorage.getItem("token");
            return (token === null ? true : false);
        }
    }
        
    
}
</script>

