<script>
import HelloWorld from './components/HelloWorld.vue'
import { NMessageProvider, NConfigProvider, NGlobalStyle } from 'naive-ui'

export default {
  name: 'App',
  data() {
    return {
    }
  },
  components: {
    HelloWorld,
    NMessageProvider,
    NConfigProvider,
    NGlobalStyle
  },
  setup() {
  }
}
</script>

<template>

  <n-config-provider theme="null">
    <n-global-style />
  </n-config-provider>

  <n-message-provider placement="bottom-right">
    <HelloWorld />
  </n-message-provider>

</template>


<style scoped>


</style>
