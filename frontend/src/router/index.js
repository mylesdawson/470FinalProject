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
import MainPage from '@/components/MainPage'
import CreateAccountPage from '@/components/CreateAccountPage'
import SearchListingsPage from '@/components/SearchListingsPage'
import SearchPage from '@/components/SearchPage'
import BookAppointmentPage from '@/components/BookAppointmentPage'
import CustomerAppointmentsPage from '@/components/CustomerAppointmentsPage'

import {
          BootstrapVue,
          IconsPlugin,
          LayoutPlugin,
          ModalPlugin,
          CardPlugin,
          VBScrollspyPlugin,
          DropdownPlugin,
          TablePlugin,
          BootstrapVueIcons
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
Vue.use(BootstrapVueIcons)
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/home',
      name: 'MainPage',
      component: MainPage,
      alias: '/',
      beforeEnter(to, from, next) {
        if (localStorage.getItem("account_type") == "customer") {
          next()
        }
        if (localStorage.getItem("account_type") == "business") {
          next({name: 'CalendarPage'})
        }
        else {
          next();
        }
      }
    },
    {
      path: '/search-listing/:id',
      name: 'SearchListingsPage',
      component: SearchListingsPage,
    },
    {
      path: '/search-listing/:business_id/book/:service_id',
      name: 'BookAppointmentPage',
      component: BookAppointmentPage,
      beforeEnter(to, from, next) {
        if (localStorage.getItem("account_type") == "customer") {
          next()
        } else {
          next(false);
        }
      }
    },
    {
      path: '/search',
      name: 'SearchPage',
      component: SearchPage,
    },
    {
      path: '/login',
      name: 'LoginPage',
      component: LoginPage,
      beforeEnter(to, from, next) {
        if (localStorage.getItem("account_type") == "customer" || localStorage.getItem("account_type") == "business") {
          next(false);
        } else {
          next();
        }
      }
    },
    {
      path: '/services',
      name: 'ServicesPage',
      component: ServicesPage,
      beforeEnter(to, from, next) {
        if (localStorage.getItem("account_type") == "business") {
          next()
        } else {
          next(false);
        }
      }
    },
    {
      path: '/calendar',
      name: 'CalendarPage',
      component: CalendarPage,
      beforeEnter(to, from, next) {
        if (localStorage.getItem("account_type") == "business") {
          next()
        } else {
          next(false);
        }
      }
    },
    {
      path: '/new-account',
      name: 'CreateAccountPage',
      component: CreateAccountPage,
      beforeEnter(to, from, next) {
        if (localStorage.getItem("account_type") == "customer" || localStorage.getItem("account_type") == "business") {
          next(false);
        } else {
          next();
        }
      }
    },
    {
      path: '/business',
      name: 'BusinessPage',
      component: BusinessPage,
      beforeEnter(to, from, next) {
        if (localStorage.getItem("account_type") == "business") {
          next()
        } else {
          next(false);
        }
      }
    },
    {
      path: '/appointments',
      name: 'CustomerAppointmentsPage',
      component: CustomerAppointmentsPage,
      beforeEnter(to, from, next) {
        if (localStorage.getItem("account_type") == "customer") {
          next()
        } else {
          next(false);
        }
      }
    }
  ],
  // turn this on if we want to get rid of # in url
  // mode: 'history'
})
