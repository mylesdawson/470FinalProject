import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import LoginPage from '@/components/LoginPage'
import TeamPage from '@/components/TeamPage'
import NewListingPage from '@/components/NewListingPage'


import {
          BootstrapVue,
          IconsPlugin,
          LayoutPlugin,
          ModalPlugin,
          CardPlugin,
          VBScrollspyPlugin,
          DropdownPlugin,
          TablePlugin
        } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(DropdownPlugin)
Vue.use(TablePlugin)
Vue.use(VBScrollspyPlugin)
Vue.use(CardPlugin)
Vue.use(ModalPlugin)
Vue.use(LayoutPlugin)
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/login',
      name: 'LoginPage',
      component: LoginPage
    },
    {
      path: '/team',
      name: 'TeamPage',
      component: TeamPage
    },
    {
      path: '/new-listing',
      name: 'NewListingPage',
      component: NewListingPage
    }
  ],
  // turn this on if we want to get rid of # in url
  // mode: 'history'
})
