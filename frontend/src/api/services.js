// URL may remain the same even in production. we may not need this code
let host = "http://localhost:8080"
if(process.env.NODE_ENV === "production") {
  host = "TODO....."
}

export async function getServices() {
  return fetch(host+'/services', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
      }
    })
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
      return data.results;
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

export async function createService(service) {
  service.price = String(service.price);
  const body = JSON.stringify(service);
  console.log(body);

  const res = await request(`/services/`, body, 'POST');
  console.log(res);
  return res;
}


  