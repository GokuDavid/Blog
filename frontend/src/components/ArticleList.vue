<template>
   <div>
    <el-row>
      <el-col :span="8">
        <div class="grid-content bg-purple" />
      </el-col>
      <el-col :span="8">
        <!-- <div class="grid-content bg-purple-light" /> -->
        <div v-for="article in articles" v-bind:key="article.id" id="articles">
          <div><span>{{ article.title }}</span> </div>
          <div>{{ article.body }}</div>
          <div>
            <div>{{ formatted_time(article.created) }}</div>
          </div>
        </div>
      </el-col>
      <el-col :span="8">
        <div class="grid-content bg-purple" />
      </el-col>
    </el-row>
  </div>
</template>

<script>
import axios from 'axios';


export default {
  name: "ArticleList",
  data: function () {
    return {
      articles: ""
    };
  },
  mounted() {
    axios
      .get("/api/article")
      .then(response => (this.articles = response.data));
  },
  methods: {
    formatted_time: function (iso_date_string) {
      const date = new Date(iso_date_string);
      return date.toLocaleDateString()
    }
  }
}
</script>

<style>
#articles {
  padding: 10px;
}

.article-title {
  font-size: large;
  font-weight: bolder;
  color: black;
  text-decoration: none;
  padding: 5px 0 5px 0;
}
</style>