// URL may remain the same even in production. we may not need this code
let host = "http://localhost:8080"
if(process.env.NODE_ENV === "production") {
  host = "TODO....."
}

export default {
    data () {
      return {
        services: [
          { name: 'Full Service', description: "Haircut, Beard trim or hot shave, and style", price: 35, duration: 40 },
          { name: 'Fade', description: "Fade haircut", price: 25, duration: 30 },
          { name: 'Beard Trim', description: "Beard trim and styling service", price: 15, duration: 20 },
          { name: 'Hair Style', description: "Hair styling service", price: 10, duration: 10 },
        ]
      }
    }
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


  