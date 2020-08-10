let host = "http://localhost:8080"
if(process.env.NODE_ENV === "production") {
  host = "TODO....."
}

function tokenHeader() {
  const token = localStorage.getItem("token")

  const header = ['Authorization', `Token ${token}`]
  return header
}

export async function getAppointments(year, month) {
  console.log(year, month)
  const token = tokenHeader()
  const business_id = localStorage.getItem("account_id")
  const headers = new Headers()
  headers.append(token[0], token[1])

  const options = {
    method: 'GET',
    headers
  }
  return fetch(host+`/business/${business_id}/appointments/month/${year}/${month+1}`, options)
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);

      return sanitizeAppointments(data);
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

// format appointments for the vue-full calendar
function sanitizeAppointments(appointmentsArray) {
  
  const newArray = appointmentsArray.filter(function (obj) {
       
    
    obj.allDay = true;

    if(obj.status == "past"){
      obj.title = `Past: ${obj.appointments} appointments`;
      obj.backgroundColor = "#6c757d";
      obj.borderColor = "#495057";
      obj.textColor = "#fff";
    }
    if(obj.status == "open"){
      obj.title = `Open: ${obj.appointments} appointments`;
      obj.backgroundColor = " #28a745";
      obj.borderColor = " #28a745";
      obj.textColor = "#fff";
    }
    if(obj.status == "unavailable"){
      obj.title = `Unavailable for booking`;
      obj.backgroundColor = "#17a2b8";
      obj.borderColor = "#17a2b8";
      obj.textColor = "#fff";
    }
    if(obj.status == "closed"){
      obj.title = `Closed`;
      obj.backgroundColor = "#dc3545";
      obj.borderColor = "#dc3545";
      obj.textColor = "#fff";
    }

    return obj;
  });

  return newArray;

}