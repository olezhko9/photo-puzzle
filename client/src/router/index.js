import Vue from 'vue'
import Router from 'vue-router'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'

import Mosaic from '@/components/Mosaic'

Vue.use(Buefy)
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Mosaic',
      component: Mosaic
    }
  ],
  mode: 'history'
})
