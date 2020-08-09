let host = "http://localhost:8080"
if(process.env.NODE_ENV === "production") {
  host = "TODO....."
}

function tokenHeader() {
  const token = localStorage.getItem("token")

  const header = ['Authorization', `Token ${token}`]
  return header
}

export async function getAppointments() {
  const token = tokenHeader()
  const business_id = localStorage.getItem("account_id")
  const headers = new Headers()
  headers.append(token[0], token[1])

  const options = {
    method: 'GET',
    headers
  }
 
  return fetch(host+`/business/${business_id}/services/available/2020/8`, options)
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
      return data;
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}


export async function getAppointmentsByDay(dateObj) {
  const token = tokenHeader()
  const business_id = localStorage.getItem("account_id")
  const headers = new Headers()
  headers.append(token[0], token[1])

  const options = {
    method: 'GET',
    headers
  }
  
  return fetch(host+`/business/${business_id}/appointments/day/${dateObj.years}/${dateObj.months+1}/${dateObj.date}/`, options)
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
      return data;
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

export async function onCancelAppointment(app_id) {
  const token = tokenHeader()
  const business_id = localStorage.getItem("account_id")
  const headers = new Headers()
  headers.append(token[0], token[1])

  const options = {
    method: 'POST',
    headers
  }
  
  return fetch(host+`/business/${business_id}/appointments/${app_id}/cancel/`, options)
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
      return data;
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}


