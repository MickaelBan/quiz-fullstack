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
            <div class="possibleAnswers" v-for="(possibleAnswer,index) in question.possibleAnswers">
                <a @click="$emit('answer-selected',index)">{{ possibleAnswer.text }}</a>
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
    padding: 20px;
    margin: 5px;
    transition-duration: 0.2s;
    display: inline-block;
    border-radius: 5px;
    border: 1px solid #4CAF50;
}
.possibleAnswers:hover {
  background-color: #4CAF50;
  color: white;
  box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
}
.possibleAnswers:active {
  background-color: #3e8e41;
  transform: translateY(4px);
}
</style>
<script>
export default {
  props: {
    question : {
        type: Object
    }
  },
  emits: ["answer-selected"]
}
</script>