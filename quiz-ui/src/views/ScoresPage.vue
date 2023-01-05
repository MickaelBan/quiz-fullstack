<template>
    <body>
        <div class="cpnt">
                <h4>Profil:</h4>
            <div class="list">
                <div class="score"><h4>Name: {{ playerName }}</h4></div>
                <div class="score"><h4>Score: {{ score }}</h4></div>
            </div>
        </div>
        <ListScoreTop :maxlist="null"/>
        <div class="button">
            <input type="submit" value="Home" v-on:click="homepage">
        </div>
    </body>
</template>

<script>
import ListScoreTop from '../components/ListScores.vue';
import ParticipationStorageService from '../services/ParticipationStorageService';

export default {
    components: {
        ListScoreTop
    },
    data(){
        var score="";
        var playerName="";
        return {
            score,playerName
        };
    },
    async created(){
        try {
            this.playerName = ParticipationStorageService.getPlayerName()
            this.score = ParticipationStorageService.getParticipationScore()
        }
        catch (error){
            console.log(error)
        }
        console.log("created Scores Page")
    },
    methods:{
        homepage(){
            this.$router.push("/")
        }
    }
    
}
</script>