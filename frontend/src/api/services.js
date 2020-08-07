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


// export async function getServices() {
  
//   const headers = new Headers()
//   headers.append("Content-Type", "application/json")

//   const options = {
//     method,
//     headers
//   };

//   return fetch(host + url, options)
//     .then(resp => resp.json())
//     .then(res => {
//       // console.log(res)
//       return res
//     })
//     .catch(err => {
//       console.log(err)
//     })

// }

export async function editService(name, description, price, duration) {
  const body = JSON.stringify(service);
  console.log(body);

  const res = await request(`/services/`, body, 'PUT');
  console.log(res);
  return res;
}

export async function createService(service) {
  const body = JSON.stringify(service);
  console.log(body);

  const res = await request(`/services/`, body, 'POST');
  console.log(res);
  return res;
}


  