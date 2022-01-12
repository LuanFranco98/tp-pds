import Vue from 'vue'
import CreateUsuario from './CreateUsuario.vue'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faPencilAlt } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faPencilAlt)

Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.config.productionTip = false

import axios from 'axios'
Vue.prototype.$http = axios
Vue.prototype.$api_url = process.env.VUE_APP_API_HOST

new Vue({
  render: h => h(CreateUsuario),
}).$mount('#app')
