<template>
    <div class="cpnt">
        <div class="question">
            <div class="imageQuestion">
                <img v-if="question.image" :src="question.image" />
            </div>
            <div class="titleQuestion">
                <h1>{{ question.title }}</h1>
            </div>
            <div class="textQuestion">
                <h3>{{ question.text }}</h3>
            </div>
            <div class="barAnswers" v-for="(possibleAnswer,index) in question.possibleAnswers">
                <a class="possibleAnswers" v-on:click="$emit('answer-selected',index+1)">{{ possibleAnswer.text }}</a>
            </div>
        </div>
    </div>
</template>
<style>
.question{   
    padding: 10px;
    text-align: center;
}
.imageQuestion{
}
.titleQuestion{
    padding: 20px;
}
.textQuestion{
}
.possibleAnswers {
    background-color: #4CAF50;
    color: white;
    padding: 14px 20px;
    margin: 5px 0;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}
.possibleAnswers:hover {
  background-color: #3e8e41;
  color: white;
  box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
}
.possibleAnswers:active {
  background-color: #3e8e41;
  transform: translateY(4px);
}
.barAnswers{
    display: inline-block;
    margin: 15px 5px
}
</style>

<script>
export default {
  props: {
    question : {
        type: Object
    }
  },
  emits: ["answer-selected"],
}
</script>

