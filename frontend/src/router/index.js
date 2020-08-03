import Vue from 'vue'
import Router from 'vue-router'
import LoginPage from '@/components/LoginPage'
import BusinessPage from '@/components/BusinessPage'
import TeamPage from '@/components/TeamPage'
import HomePage from '@/components/HomePage'
import ServicesPage from '@/components/ServicesPage'
import NewListingPage from '@/components/NewListingPage'
import CalendarPage from '@/components/CalendarPage'
import ListingsPage from '@/components/ListingsPage'

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

import FullCalendar from "vue-full-calendar";
import "fullcalendar/dist/fullcalendar.min.css";
import VModal from 'vue-js-modal'

Vue.use(VModal)
Vue.use(FullCalendar);
Vue.config.productionTip = false;

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
      path: '/home',
      name: 'HomePage',
      component: HomePage,
      alias: '/' 
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
      path: '/services',
      name: 'ServicesPage',
      component: ServicesPage
    },
    {
      path: '/calendar',
      name: 'CalendarPage',
      component: CalendarPage
    },
    {
      path: '/listings',
      name: 'ListingsPage',
      component: ListingsPage
    },
    {
      path: '/new-listing',
      name: 'NewListingPage',
      component: NewListingPage
    },
    {
      path: '/business',
      name: 'BusinessPage',
      component: BusinessPage
    }
  ],
  // turn this on if we want to get rid of # in url
  // mode: 'history'
})
