<template>

    <component v-if="parts" :is="pages[parts.page]"/>
    <pre>{{route.params}}</pre>
    <pre>{{route.path}}</pre>
    <pre>{{parts}}</pre>
</template>

<script setup>
import { onMounted, ref, watch } from 'vue';
import { useRoute } from 'vue-router';
import post from "./postPage.vue";
import posts from "./postsPage.vue";

const pages = {
  post: post,
  posts: posts,
}

const route = useRoute()
const parts = ref(null);


const splitRoute = () =>{
  if(route.path){
    let arr = route.path.split("/").slice(1);
    //arr.reverse();
    parts.value = {
      module: arr[0],
      page: arr[1],
      component: arr[2] || null,
      slug: arr[3] || null,
    };
  }
}

onMounted(()=>{
  splitRoute();
});

watch(route,()=>{
  splitRoute();

})





</script>

<style lang="scss" scoped>


</style>
