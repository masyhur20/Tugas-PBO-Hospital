### SIMULASI RUMAH SAKIT ###

### NAMA    : M. MUSTHOFA MASYHUR           DOSEN PENGAMPU  : MUHAMMAD AFFANDES, S.T, M.T.
### NIM     : 12550111055                   MATA KULIAH     : PEMROGRAMAN BERORIENTASI OBJEK
### KELAS   : B                             TUGAS           : 3

# DOCTOR CLASS TO REPRESENT A DOCTOR IN THE HOSPITAL

class Doctor:
    def __init__(self, name, doctor_id, speciality):
        self.name = name
        self.doctor_id = doctor_id
        self.speciality = speciality

    def __str__(self):
        return (f"Dr. {self.name}, {self.speciality}")
    

# PATIENT CLASS TO REPRESENT A PATIENT

class Patient:
    def __init__(self, name, patient_id):
        self.name = name
        self.patient_id = patient_id
        self.appointments = []

    def make_appointments(self, doctor, appointment_date):
        appointment = Appointment(self, doctor, appointment_date)
        self.doctor = doctor
        self.appointments.append(appointment)
        print(f"\n- Appointment made for {self.name}, with Dr. {doctor.name} on {appointment_date}")


# APPOINTMENT CLASS TO REPRESENT AN APPOINTMENT BETWEEN A PATIENT AND A DOCTOR

class Appointment:
    def __init__(self, patient, doctor, appointment_date):
        self.patient = patient
        self.doctor = doctor
        self.appointment_date = appointment_date
        self.treatments = []

    def add_treatment(self, treatment_name, treatment_date):
        treatment = Treatment(self, treatment_name, treatment_date)
        self.treatments.append(treatment)
        print(f"\n- Treatment '{treatment_name}' added for appointment on {self.appointment_date}")


# TREATMENT CLASS TO REPRESENT A TREATMENT PROVIDED DURING AN APPOINTMENT

class Treatment:
    def __init__(self, appointment, treatment_name, treatment_date):
        self.appointment = appointment
        self.treatment_name = treatment_name
        self.treatment_date = treatment_date

    def __str__(self):
        return (f"Treatment: {self.treatment_name} on {self.treatment_date}")
    