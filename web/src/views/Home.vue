<template>
  <a-layout-content style="padding: 0 50px">
    <a-breadcrumb style="margin: 16px 0">
      <a-breadcrumb-item>Home</a-breadcrumb-item>
      <a-breadcrumb-item>List</a-breadcrumb-item>
      <a-breadcrumb-item>App</a-breadcrumb-item>
    </a-breadcrumb>
    <div :style="{ background: '#fff', padding: '24px', minHeight: '280px' }">
      {{ articles }}
    </div>
  </a-layout-content>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import axios from "axios";
// import HelloWorld from "@/components/HelloWorld.vue"; // @ is an alias to /src

export default defineComponent({
  name: "Home",
  setup(){
    const articles = ref()
    console.log("setup")
    axios.get("/api/article/").then(
        (response)=>{
          articles.value = response.data;
        }
    );  
    return {
    articles,
    }
  },
});
</script>
