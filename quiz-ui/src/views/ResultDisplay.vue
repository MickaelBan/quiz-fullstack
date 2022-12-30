<template>
    <div class="cpnt">
        <h2>Score: {{ score }}</h2>
    </div>
    <div class="cpnt">
        <h2>Correct answers - if you have correct</h2> 
        <div class="score" v-for="answer in answersSummaries">
            <h6>{{ answer.correctAnswerPosition }} - {{ answer.isCorrect }}</h6>
        </div>
    </div>
</template>

<style>
</style>

<script>
import ParticipationStorageService from "../services/ParticipationStorageService";
import QuizApiService from "../services/QuizApiService";

export default {
    props:{
        answersSummaries: {
            type: Object
        },
        playerName : String,
        score: Number
    }
}
</script>