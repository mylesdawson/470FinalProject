let host = "http://localhost:8080"

function tokenHeader() {
  const token = localStorage.getItem("token")

  const header = ['Authorization', `Token ${token}`]
  return header
}

export async function getBusiness() {
  const token = tokenHeader()
  const headers = new Headers()
  const business_id = localStorage.getItem("account_id")
  headers.append(token[0], token[1])

  const options = {
    method: 'GET',
    headers
  }

  return fetch(host+`/business/${business_id}/`, options)
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
      return data;
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

export async function editBusiness(obj, type) {
  const token = tokenHeader()
  const headers = new Headers({
    'Content-Type': 'application/json',
    'Accept': 'application/json',

  })
  const business_id = localStorage.getItem("account_id")
  headers.append(token[0], token[1])

  const options = {
    method: 'POST',
    headers,
    body: JSON.stringify(obj)
  }

  return fetch(host+`/business/${business_id}/edit/${type}/`, options)
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
      return data;
    })
    .catch((error) => {
      console.error('Error:', error);
    });
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
  headers.append("Content-Type", "application/json")
  const business_id = localStorage.getItem("account_id")
  headers.append(token[0], token[1])

  // console.log(service)
  // console.log(JSON.stringify(service))

  const options = {
    method: 'POST',
    headers,
    body: JSON.stringify(service)
  }

  return fetch(host+`/business/${business_id}/services/new/`, options)
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

  return fetch(host+`/business/${business_id}/services/${service_id}/delete/`, options)
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


