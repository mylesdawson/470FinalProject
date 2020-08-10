
// URL may remain the same even in production. we may not need this code
let host = "http://localhost:8080"
if(process.env.NODE_ENV === "production") {
  host = "TODO....."
}


/*
  Sexy generic request function from:
  https://dev.to/eddieaich/create-an-awesome-js-api-interface-using-fetch-in-less-than-50-lines-3d65
  Eventually we will need other functions for sending non-json data
*/
async function request(url, body = {}, method = 'GET') {
  console.log(`request to: ${url}`)

  const headers = new Headers()
  headers.append("Content-Type", "application/json")

  const options = {
    method,
    headers
  };

  if (method !== 'GET' && body) {
    options.body = JSON.stringify(body)
  }

  return fetch(host + url, options)
    .then(resp => resp.json())
    .then(res => {
      // console.log(res)
      return res
    })
    .catch(err => {
      console.log(err)
    })

}

function tokenHeader() {
  const token = localStorage.getItem("token")

  const header = ['Authorization', `Token ${token}`]
  return header
}

/* Requests to API endpoints go here */

export async function login(username = '', password = '') {
  const body = {
    username,
    password
  }

  const headers = new Headers()
  headers.append("Content-Type", "application/json")

  const options = {
    method: 'POST',
    headers,
    body: JSON.stringify(body)
  }

  return fetch(`${host}/login/`, options)
    .then(resp => {
      // console.log(resp)
      return resp.json()
    })
    .then(res => {
      console.log(res)
      localStorage.setItem('token', res.token)
      localStorage.setItem('account_type', res.account_type)
      localStorage.setItem('account_id', res.account_id)
      localStorage.setItem('user_id', res.user_id)
      return res
    })
    .catch(err => {
      console.log(err)
    })

}

export async function logout() {
  const token = tokenHeader()
  const headers = new Headers()
  headers.append(token[0], token[1])

  const options = {
    method: 'POST',
    headers
  }
  console.log('logging out')

  return fetch(`${host}/logout/`, options)
    .then(resp => {
      if(resp.status === 200) {
        localStorage.removeItem("token")
        localStorage.removeItem("account_id")
        localStorage.removeItem("account_type")
        localStorage.removeItem("user_id")
      }
      return resp.status
    })
    .catch(err => {
      console.log(err)
    })
}

export async function createCustomerAccount(username, password, accountInfo) {
  // console.log(`accountType: ${accountType}, username: ${username}, password: ${password}`)
  // console.log(JSON.stringify(accountInfo))

  const body = {
    username,
    password,
    customer: accountInfo
  }

  const res = await request(`/customers/`, body, 'POST')
  console.log(res)
  return res
}

export async function createBusinessAccount(username, password, accountInfo) {
  const body = {
    username,
    password,
    business: accountInfo
  }

  const res = await request(`/businesses/`, body, 'POST')
  console.log(res)
  return res
}


export async function users() {
  const res = await request('/users/')
  console.log(res)
}

const categories = {
  fitness: 'fitness',
  wellness: 'wellness',
  beauty: 'beauty',
  all: 'all'
}
export async function getBusinessesByCategory(category = 'all') {
  const headers = new Headers()
  headers.append("Content-Type", "application.json")

  const options = {
    headers,
  }

  return fetch(`${host}/business/search/${category}/`, options)
    .then(res => res.json())
    .then(res => res)
    .catch(e => {
      console.log(e)
    })
}

export async function getServicesByBusiness(business_id) {
  const headers = new Headers()
  headers.append("Content-Type", "application.json")

  const options = {
    headers,
  }

  return fetch(`${host}/business/${business_id}/services/`, options)
    .then(res => res.json())
    .then(res => res)
    .catch(e => {
      console.log(e)
    })
}

export async function getBusinessInfo(business_id) {
  const headers = new Headers()
  headers.append("Content-Type", "application.json")

  const options = {
    headers,
  }

  return fetch(`${host}/business/${business_id}/`, options)
  .then(res => res.json())
  .then(res => res)
  .catch(e => {
    console.log(e)
  })
}

export async function getAvailableTimeSlots(business_id, year, month, day) {

  return fetch(`${host}/business/${business_id}/services/available/${year}/${month}/${day}`)
  .then(res => res.json())
  .then(res => res)
  .catch(e => {
    console.log(e)
  })
}