
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

  const options = {
    method,
    headers: {
      'Content-Type': 'application/json'
    }
  };

  if (body) {
      options.body = JSON.stringify(body);
  }

  const response = await fetch(host + url, options);

  if (response.status !== 200) {
    return generateErrorResponse('The server responded with an unexpected status.');
  }

  const result = await response.json();

  return result;
}


/* Requests to API endpoints go here */

export async function login(username = '', password = '') {
  console.log(`username: ${username}, password: ${password}`)
  const res = await request(`${host}/login`, { username, password })
  console.log(res)
}
