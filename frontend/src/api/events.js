export default {
    data () {
      return {
        events: [
            {
                start: '2020-08-02T12:30:00',
                end: '2020-08-02T13:30:00',
                title: 'my event',
                allDay: false,
                id: null,
                url: null,
                backgroundColor:null,
                borderColor:null,
                textColor:null,
                extendedProps: {
                    listing: null,
                    service: null,
                    employee: null,
                    price: null,
                  }
              }
      
          ],
      }
    }
  }
  
let host = "http://localhost:8080"
if(process.env.NODE_ENV === "production") {
  host = "TODO....."
}

export async function getAppointments() {
  return fetch(host+'/appointments/', {
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


export async function getAppointmentsByDay(dateObj) {

  const business_id = 1;
  return fetch(host+`/business/${business_id}/appointments/day/${dateObj.years}/${dateObj.months+1}/${dateObj.date}/`, {
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