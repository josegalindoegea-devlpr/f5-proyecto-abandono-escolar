# 1	Definición del Dataset
Version_interna: 2.0
## 1.1	Definición dataset
El dataset tendrá la utilidad de ser la entrada al modelo de la operativa de “abandono escolar”.
## 1.2	Variables necesarias
Las variables mínimas del dataset se describen a continuación:
Académicas:
•	asistencia_pct: entero, porcentaje de asistencia
•	nota_media:  decimal, promedio de calificaciones
•	materias_suspensas: entero, numero de asignaturas no aprobadas
•	numero_materias_curso: entero, número de asignaturas totales del curso
•	evaluaciones_realizadas: entero, número de evaluaciones realizadas.
•	partes_disciplinarios: entero, número total de amonestaciones durante el curso actual.
Administrativa:
•	matricula_activa: booleano, 1 sí, 0 no
•	oferta_educativa: entero, 1 -> ESO; 2 -> Bachillerato; 3 -> FP Básica; 4 -> FP Grado Medio.
•	Repetidor_curso_actual: booleano, 1 sí, 0 no.
Comportamiento temporal:
•	días_sin_actividad: entero, días sin registro educativo
•	inasistencias_consecutivas: entero, faltas seguidas
Demograficas:
•	grado_urbanización: entero, 1 -> Rural; 2 -> Semiurbano; 3 -> Urbano
Socio-educativas:
•	distancia_escuela: decimal, distancia en KM con la escuela
•	acceso_internet: booleano (1 sí, 0 no)
•	nivel_socioeconomico: entero, asociado a la clase social, 1-> Alta; 2->Media Alta; 3-> Media; 4->Media Baja; 5-> Baja Alta; 6-> Baja Baja
•	apoyo_familiar: booleano (1 sí, 0 no)
•	trabaja: booleano (1 sí, 0 no)

## 1.3	Reglas de carga
•	Si matricula_activa == 0, el resto de las variables tienes poca importancia, pues será un registro a desechar.
•	El máximo de dias_sin_actividad será el valor 65
•	Si nota_media estará entre 0.0 y 10.0
•	Si asistencia_pct estará entre 0.0 y 100.0
•	Si materias_suspensas estará entre 0 y 10.
•	Si numero_materias_curso estará entre 10, 11,12, 13 y 14.
•	Si evaluaciones_realizadas estará entre 0 y 4.
•	Si partes_disciplinarios estará entre 0 y 10.
•	Si distancia_escuela estará entre 1 y 50.
•	Si días_sin_actividad estará entre 1 y 65.
•	Si inasistencias_consecutivas estará entre 1 y 65.
---