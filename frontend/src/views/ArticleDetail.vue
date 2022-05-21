<template>

    <BlogHeader />
    <el-page-header @back="goBack" />

    <div v-if="article !== null" class="grid-container">
        <div>
            <h1 id="title">{{ article.title }}</h1>
            <p id="subtitle">
                本文由 {{ article.author.username }} 发布于 {{ formatted_time(article.created) }}
            </p>
            <div v-html="article.body_html" class="article-body"></div>
        </div>
         <div>
            <h3>目录</h3>
            <div v-html="article.toc_html" class="toc"></div>
        </div>
    </div>

    <BlogFooter />

</template>

<script>
import axios from 'axios';
import BlogHeader from '@/components/BlogHeader.vue'
import BlogFooter from '@/components/BlogFooter.vue'

export default {
    name: 'ArticleDetail',
    components: { BlogHeader, BlogFooter },
    data: function () {
        return {
            article: null
        }
    },
    mounted() {
        axios
            .get('/api/article/' + this.$route.params.id)
            .then(response => (this.article = response.data))
    },
    methods: {
        formatted_time: function (iso_date_string) {
            const date = new Date(iso_date_string);
            return date.toLocaleDateString()
        },
        goBack(){
        if (window.history.length <= 1) {
            this.$router.push({path:'/'})
            return false
        } else {
            this.$router.go(-1)
        }
    }
    }
}
</script>

<style>
    .article-body p img {
        max-width: 100%;
        border-radius: 50px;
        box-shadow: gray 0 0 20px;
    }

</style>