### SIMULASI RUMAH SAKIT ###

### NAMA    : M. MUSTHOFA MASYHUR           DOSEN PENGAMPU  : MUHAMMAD AFFANDES, S.T, M.T.
### NIM     : 12550111055                   MATA KULIAH     : PEMROGRAMAN BERORIENTASI OBJEK
### KELAS   : B                             TUGAS           : 3

from Hospital_3 import Doctor, Patient, Appointment, Treatment


# KELAS DOKTER

doctor_1 = Doctor("Julia Meade, M.D., FAAD", "DOC-CAD-002", "Clinical & Aesthetic Dermatology")
doctor_2 = Doctor("Ilsa Faust, MBBS, MRCP, FAMS", "DOC-DER-095", "Dermatovenereologist")

print(" ")
print("=== TODAY'S DOCTOR SCHEDULE ===")
print(" ")
print(doctor_1)
print(doctor_2)
print(" ")
print("=== MOUNT ELIZABETH HOSPITAL ===")


# KELAS PATIENT

patient_1 = Patient ("Paris Lim", "PAT-001")
patient_2 = Patient ("Jane Carter", "PAT-002")
patient_3 = Patient ("Grace Lim", "PAT-003")
patient_4 = Patient ("Alanna Mitsopolis", "PAT-004")

print(f"\nAPPOINTMENT INFORMATION: ")
patient_1.make_appointments(doctor_1, "22-02-2026")
patient_2.make_appointments(doctor_1, "22-02-2026")
patient_3.make_appointments(doctor_2, "22-02-2026")
patient_4.make_appointments(doctor_2, "22-02-2026")


# KELAS APPOINTMENT

appointment_1 = patient_1.appointments[0]
appointment_2 = patient_2.appointments[0]
appointment_3 = patient_3.appointments[0]
appointment_4 = patient_4.appointments[0]
#appointment_5 = patient_4.appointments[0]

print(f"\nTREATMENT INFORMATION: ")
appointment_1.add_treatment("Chemical Peeling", "27-02-2026")
appointment_2.add_treatment("Injectables", "27-02-2026")
appointment_3.add_treatment("Laser Rejuvenation", "27-02-2026")
appointment_4.add_treatment("Facial & Resurfacing", "27-02-2026")
#appointment_4.add_treatment("Injectables", "27-02-2026")

