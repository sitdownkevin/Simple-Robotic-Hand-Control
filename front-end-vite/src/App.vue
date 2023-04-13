<script>
import HelloWorld from './components/HelloWorld.vue'


export default {
  name: 'App',
  data() {
    return {
      theme: null
    }
  },
  components: {
    HelloWorld
  },
  // setup() {
  //   return {
  //     darkTheme
  //   };
  // }
}
</script>

<template>
  <n-config-provider theme="null">
    <n-global-style />
  </n-config-provider>
  <!-- <n-config-provider :theme="theme">
    <n-global-style /> -->
    <!-- <n-card>
      <n-space>
        <n-button @click="theme = darkTheme">
          深色
        </n-button>
        <n-button @click="theme = null">
          浅色
        </n-button>
      </n-space>
    </n-card> -->
    <HelloWorld />
  <!-- </n-config-provider> -->
  <!-- <HelloWorld /> -->
</template>


<style scoped>


</style>
