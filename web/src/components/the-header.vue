<template>
    <a-layout-header>
      <div class="logo" />
      <a-menu
        v-model:selectedKeys="selectedKeys"
        theme="dark"
        mode="horizontal"
        :style="{ lineHeight: '64px' }"
      >
        <a-menu-item key="/"><router-link to="/">首页</router-link></a-menu-item>
        <a-menu-item key="2">nav 2</a-menu-item>
        <a-menu-item key="/about"><router-link to="/about">关于我们</router-link></a-menu-item>
      </a-menu>
    </a-layout-header>
</template>

<script lang="ts">
import { defineComponent,ref} from "vue";
export default defineComponent({
  name: "the-header",
    setup() {
    return {
      selectedKeys: ref<string[]>(['2']),
    };
  },
});
</script>