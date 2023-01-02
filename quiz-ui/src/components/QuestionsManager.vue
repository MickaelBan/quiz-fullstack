<template>
    <div v-if="!hiden">
        <div class="title">
            <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
        </div>
        <body>
            <QuestionDisplay :question="currentQuestion" @answer-selected="answerClickedHandler" />
        </body>
    </div>
    <div v-else>
        <div class="title">
            <h1>Answers summary of {{ playerName }}</h1>
        </div>
        <body>
            <resultDisplay :answersSummaries="answersSummaries" :playerName="playerName" :score="score"/>
            <div class="button">
                <input type="submit" value="scores" v-on:click="scoresPage">
            </div>
        </body>
    </div> 
</template>

<script>
import QuestionDisplay from '../views/QuestionDisplay.vue';
import QuizApiService from '../services/QuizApiService';
import ParticipationStorageService from '../services/ParticipationStorageService';
import resultDisplay from '../views/ResultDisplay.vue';

export default { 
    components: {
        QuestionDisplay,
        resultDisplay
    },
    data() {
        var currentQuestion = {
            id: 0,
            title: "",
            text: "",
            image: "",
            position: 0,
            possibleAnswers: []
        };
        var currentQuestionPosition = 0;
        var totalNumberOfQuestion = 0;
        var listAnswers = [];
        var answersSummaries = [];
        var score = 0;
        var playerName = '';
        var hiden = false;

        return {
            currentQuestion,currentQuestionPosition,totalNumberOfQuestion,listAnswers,
            answersSummaries,score,playerName,hiden
        };
    },    
    async created() {
        this.currentQuestionPosition  = 1 ;
        this.currentQuestion = await this.loadQuestionByPosition(this.currentQuestionPosition)
        var reponce = await QuizApiService.getQuizInfo()
        this.totalNumberOfQuestion = reponce.data.size
        this.playerName = ParticipationStorageService.getPlayerName()
        console.log("question manager created")
    },
    methods:{
        async loadQuestionByPosition(position){
            let reponse = await QuizApiService.getQuestionByPosition(position)
            return reponse.data
        },
        async answerClickedHandler(answer){
            this.listAnswers.push(answer);            
            this.currentQuestionPosition += 1;
            if (this.currentQuestionPosition > this.totalNumberOfQuestion){
                this.endQuiz()
            }
            else {
                this.currentQuestion = await this.loadQuestionByPosition(this.currentQuestionPosition);
            }
        },
        async endQuiz(){
            var reponce = await QuizApiService.postParticipation(
                this.playerName,this.listAnswers
            );
            this.answersSummaries = reponce.data.answersSummaries;
            this.score = reponce.data.score;
            this.hiden = true
            ParticipationStorageService.saveParticipationScore(this.score)
        },
        scoresPage(){
            this.$router.push("/scores")
        }
        
    }

}
</script>