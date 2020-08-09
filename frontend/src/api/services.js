// URL may remain the same even in production. we may not need this code
let host = "http://localhost:8080"
if(process.env.NODE_ENV === "production") {
  host = "TODO....."
}

function tokenHeader() {
  const token = localStorage.getItem("token")

  const header = ['Authorization', `Token ${token}`]
  return header
}

export async function getServices() {
  const token = tokenHeader()
  const headers = new Headers()
  const business_id = localStorage.getItem("account_id")
  headers.append(token[0], token[1])

  const options = {
    method: 'GET',
    headers
  }

  return fetch(host+`/business/${business_id}/services/`, options)
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
      return data;
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

export async function createService(service) {
  const token = tokenHeader()
  const headers = new Headers()
  const business_id = localStorage.getItem("account_id")
  headers.append(token[0], token[1])

  const options = {
    method: 'POST',
    headers,
    body: JSON.stringify(service)
  }

  return fetch(host+`/business/${business_id}/services/new`, options)
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
      return data;
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

export async function deleteService(service_id) {
  const token = tokenHeader()
  const headers = new Headers()
  const business_id = localStorage.getItem("account_id")
  headers.append(token[0], token[1])

  const options = {
    method: 'DELETE',
    headers
  }

  return fetch(host+`/business/${business_id}/services/${service_id}/delete`, options)
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
      return data;
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

export async function editService(service) {
  service.price = String(service.price);
  const body = JSON.stringify(service);
  console.log(body);

  const res = await request(`/services/`, body, 'PUT');
  console.log(res);
  return res;
}


  