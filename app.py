import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import math as mt

T1 = st.number_input("Ingresa la temperatura caliente T1: ")
T2 = st.number_input("Ingresa la temperatura caliente T2: ")
t1 = st.number_input("Ingresa la temperatura fría t1: ")
t2 = st.number_input("Ingresa la temperatura fría t2: ")
Rd_prob = st.number_input("Ingresa el valor de Rd del problema", format="%.4f")
L = st.number_input("Ingresa el valor de L del problema")

#============================
st.header("Temperaturas y Cp")
#============================
hidrocarburo = st.selectbox("¿Es un hidrocarburo? (Y/N): ", options=["Y", "N"])
if hidrocarburo == "Y":
    API_c = st.number_input("Ingresa el valor del API para la sustancia caliente: ")
    API_f = st.number_input("Ingresa el valor del API para la sustancia fría: ")

    diferencia_de_temperatura = st.selectbox("La diferencias de temperatura son mayores a 50°F? (Y/N): ", options=["Y", "N"])
    if diferencia_de_temperatura == "Y":
        diferencia_T = float(T1 - T2)
        diferencia_t = float(t2 - t1)

        st.write("La diferencia de temperatura para la sustancia caliente es: ", diferencia_T)
        st.write("La diferencia de temperatura para la sustancia fria es: ", diferencia_t)
        st.write("Nota: En caso de una ser menor a 50, el valor de Kc ponerlo como 0 y tomar de base el otro")
        st.write("Encontrar valores de Kc en la grafica llamada Temperaturas caloricas")

        Kc_c = st.number_input("Ingrasa el dato de Kc con la temeratura caliente: ")
        Kc_f = st.number_input("Ingrasa el dato de Kc con la temeratura fria: ")
        tc_th = float((T2 - t1)/(T1 - t2))

        st.write("El valor de tc/th es: ", tc_th)
        st.write("Recuerda que el valor de Kc para la sustancia caliente es de: ", Kc_c)
        Fc_c = st.number_input("Ingresa el valor de Fc para la sustancia caliente: ")

        st.write("El valor de tc/th es: ", tc_th)
        st.write("Recuerda que el valor de Kc para la sustancia fria es de: ", Kc_f)
        Fc_f = st.number_input("Ingresa el valor de Fc para la sustancia fria: ")

        Fc = st.number_input("El valor de Fc a utilizar sera el mas grande de los dos, ingresa el valor: ")
        T_ref = float(T2 + Fc * (T1 - T2))
        t_ref = float(t1 + Fc * (t2 - t1))
        st.write("la temperatura calorifica para la corriente caliente es de: ", T_ref)
        st.write("la temperatura calorifica para la corriente fria es de: ", t_ref)

        st.write("para obtener el Cp de la sustancia caliente utiliza el valor sus °API y tu temperatura calorifica")
        Cp_c = st.number_input("Ingresa el valor de Cp para la sustancia caliente: ")
        Cp_f = st.number_input("Ingresa el valor de Cp para la sustancia fria: ")
    else:
        T_ref = float((T1 + T2) / 2)
        t_ref = float((t1 + t2) / 2)
        st.write("Con la grafica de cp de liquidos y la temperatura media, encuentra los valores de los cp")
        st.write("La temperatura media de la corriente caliente es de: ", T_ref)
        Cp_c = st.number_input("Ingresa el valor de Cp para la sustancia caliente: ")
        st.write("La temperatura media de la corriente fria es de: ", t_ref)
        Cp_f = st.number_input("Ingresa el valor de Cp para la sustancia fría: ")
else:
    T_ref = float((T1 + T2) / 2)
    t_ref = float((t1 + t2) / 2)
    st.write("Con la grafica de cp de liquidos y la temperatura media, encuentra los valores de los cp")
    st.write("La temperatura media de la corriente caliente es de: ", T_ref)
    Cp_c = st.number_input("Ingresa el valor de Cp para la sustancia caliente: ")
    st.write("La temperatura media de la corriente fria es de: ", t_ref)
    Cp_f = st.number_input("Ingresa el valor de Cp para la sustancia fría: ")

#===========================
st.header("Balance de materia")
#============================
Balance_de_materia = st.selectbox("¿Tienes ambas corrientes? (Y/N)", options=["Y", "N"])
if Balance_de_materia == "Y":
    m_c = st.number_input("Ingresa el valor del flujo de la sustancia caliente: ")
    m_f = st.number_input("Ingresa el valor del flujo de la sustancia fría: ")
    Q_1 = float(m_c * Cp_c * (T1 - T2))
    st.write("El valor de Q para la sustancia caliente es de: ", Q_1)
    Q_2 = float(m_f * Cp_f * (t2 - t1))
    st.write("El valor de Q para la sustancia fría es de: ", Q_2)
    Q = st.number_input("El valor a elegir de Q sera el mayor entre Q1 y Q2: ")
else:
    cual_flujo_falta = st.selectbox("¿Cuál flujo falta? (caliente/fría): ", options=["caliente", "fría"])
    if cual_flujo_falta == "caliente":
        m_f = st.number_input("Ingresa el valor del flujo de la sustancia fría: ")
        m_c = float((m_f * Cp_f * (t2 - t1)) / (Cp_c * (T1 - T2)))
        st.write("El flujo de la sustancia caliente es de: ", m_c)
        Q = float(m_f * Cp_f * (t2 - t1))
        st.write("El valor de Q para la sustancia fría es de: ", Q)
    else:
        m_c = st.number_input("Ingresa el valor del flujo de la sustancia caliente: ")
        m_f = float((m_c * Cp_c * (T1 - T2)) / (Cp_f * (t2 - t1)))
        st.write("El flujo de la sustancia fría es de: ", m_f)
        Q = float(m_c * Cp_c * (T1 - T2))
        st.write("El valor de Q para la sustancia caliente es de: ", Q)


#================================
st.header("Cálculo de ▲TmL o ▲T")
#================================
n_c = st.slider("Número de corrientes calientes: ", min_value=1, max_value=10, value=1)
n_f = st.slider("Número de corrientes frías: ", min_value=1, max_value=10, value=1)
if n_c == 1 and n_f == 1:
    delta_TmL1 = float(T1 - t2)
    delta_TmL2 = float(T2 - t1)
    delta_T = float((delta_TmL1 - delta_TmL2) / mt.log(delta_TmL1 / delta_TmL2))
    st.write("El valor de ▲TmL es: ", delta_T)
elif n_c == 1 and n_f > 1:
    P_prima = float((T2-t1)/(T1 - t1))
    st.write("El valor de P' es: ", P_prima)
    R_prima = float((T1 - T2)/(n_f * (t2 - t1)))
    st.write("El valor de R' es: ", R_prima)
    parte_1 = float(2.3 * (n_f * R_prima)/(R_prima - 1))
    parte_2 = float(mt.log10(((R_prima-1)/(R_prima)) * ((1)/(P_prima))**(1/n_f) + (1/R_prima)))
    parte_3 = float(1 - P_prima)
    gamma = float((parte_3) / (parte_1 * parte_2))
    st.write("El valor de gamma es: ", gamma)
    delta_T = float(gamma * (T1 - t1))
    st.write("El valor de ▲T es: ", delta_T)
else:
    P_prima = float((T1-t2)/(T1-t1))
    st.write("El valor de P'' es: ", P_prima)
    R_prima = float((n_c * (T1 - T2))/(t2 -t1))
    st.write("El valor de R'' es: ", R_prima)
    parte_1 = float(2.3 * (n_c / (1-R_prima)))
    parte_2 = float(mt.log10((1-R_prima) * (1/P_prima)**(1/n_c) + R_prima))
    parte_3 = float(1 - P_prima)
    gamma = float( (parte_3) / (parte_1 * parte_2))
    st.write("El valor de gamma es: ", gamma)
    delta_T = float(gamma * (T1 - t1))
    st.write("El valor de ▲T es: ", delta_T)

#==========================
st.header("Diametros y areas de flujos")
#==========================


st.write("ingresa los valores de las tuberias IPS (herramienta en excel)")

#para tubo externo (a)
st.write("Tubo externo (a)")
Dnom = st.number_input("Ingresa el diametro nominal para tubo externo", format="%.4f")
DE = st.number_input("Ingresa el diametro externo para tubo externo", format="%.4f")
DI = st.number_input("Ingresa el diametro interno para tubo externo", format="%.4f")
AREA = st.number_input("Ingresa el area de la tuberia para tubo externo", format="%.4f")

#para tubo interno (p)
st.write("Tubo interno (p)")
dnom = st.number_input("Ingresa el diametro nominal para tubo interno", format="%.4f")
dE = st.number_input("Ingresa el diametro externo para tubo interno", format="%.4f")
dI = st.number_input("Ingresa el diametro interno para tubo interno", format="%.4f")
area = st.number_input("Ingresa el area de la tuberia para tubo interno", format="%.4f")
SL = st.number_input("Ingresa el espacio libre (SL)", format="%.4f")

if m_c > m_f:
    m_mayor = 0
    m_menor = 0
    T_ref_mayor = 0
    T_ref_menor = 0
    Cp_mayor = 0
    Cp_menor = 0
    Cp_mayor = Cp_c
    Cp_menor = Cp_f
    m_mayor = m_c
    T_ref_mayor = T_ref
    m_menor = m_f
    T_ref_menor = t_ref
    st.write("El flujo mayor es el flujo caliente y el flujo menor es el flujo frio")
else:
    m_mayor = 0
    m_menor = 0
    T_ref_mayor = 0
    T_ref_menor = 0
    Cp_mayor = 0
    Cp_menor = 0
    Cp_mayor = Cp_f
    Cp_menor = Cp_c
    m_mayor = m_f
    T_ref_mayor = t_ref
    m_menor = m_c
    T_ref_menor = T_ref
    st.write("el flujo mayor es el flujo frio y el flujo menor es el flujo caliente")

A_p = float(area/144)
st.write("El area de la tuberia interna (A_p) es de: ", A_p)
D_p = float(dI/12)
st.write("El diametro interno de la tuberia (D_p) es de: ", D_p)
numero_de_division_p = st.number_input("Ingresa el número de división para el flujo interno (n): ")
G_p = float((m_mayor/numero_de_division_p )/A_p)
st.write("El flux masico Gp es de: ", G_p)

A_a = float(((mt.pi / 4) * (DI**2 - dE**2))/144)
st.write("El area de la tuberia externa (A_a) es de: ", A_a)
D_eq = float(((DI**2 - dE**2) / dE)/12)
st.write("El diametro interno de la tuberia (D_eq) es de: ", D_eq)
numero_de_divisiones_a = st.number_input("Ingresa el número de división para el flujo en el anulo (n): ")
G_a = float((m_menor/numero_de_divisiones_a )/A_a)
st.write("El flux masico Ga es de: ", G_a)

#==========================
st.header("Viscosidades y valores de K")
#==========================

st.write("Ingresa las viscosidades de ambas sustancias a la temperatura de referencia en la grafica viscosidades de liquidos")
st.write("Para el fluido en el tubo interno (p)", m_mayor)
mu_p = st.number_input("Ingresa la viscosidad del fluido en el tubo interno (mu_p)", format="%.4f")
st.write("Para el fluido en el anulo (a)", m_menor)
mu_a = st.number_input("Ingresa la viscosidad del fluido en el anulo (mu_a)", format="%.4f")
mu_p = mu_p * 2.42
mu_a = mu_a * 2.42


st.write("Para encontrar los valores para los K puedes obtenerlos interpolando en la tabla Conductividad termica para liquidos y si es un hidrocarburo desde la grafica")
K_p = st.number_input("Ingresa el valor de K para el fluido en el tubo interno (K_p)", format="%.4f")
K_a = st.number_input("Ingresa el valor de K para el fluido en el anulo (K_a)", format="%.4f")

#==============================
st.header("Valores de números adimencionales y valor de hi_a y hi_p")
#==============================

Re_a = float((G_a * D_eq) / mu_a)
st.write("El número de Reynolds para el fluido en el anulo es de: ", Re_a)
Prandtl_a = float((Cp_menor * mu_a) / K_a)
st.write("El número de Prandtl para el fluido en el anulo es de: ", Prandtl_a)

Re_p =  float((G_p * D_p) / mu_p)
st.write("El número de Reynolds para el fluido en el tubo interno es de: ", Re_p)
Prandtl_p = float((Cp_mayor * mu_p) / K_p) 
st.write("El número de Prandtl para el fluido en el tubo interno es de: ", Prandtl_p)

st.write("Si el valor de la o las viscosidades es mucho mayor a la del agua, se corrige la viscosidad")
corregir_viscosidad = st.selectbox("¿Quieres corregir la viscosidad? (Y/N)", ["Y","N"])

if corregir_viscosidad == "Y":
    st.write("Utiliza el excel de apoyo para obtener la viscosidad corregida mu_w")
    mu_w_a = st.number_input("Ingresa el valor de la viscosidad corregida (mu_w_a)") * 2.42
    mu_w_p = st.number_input("Ingresa el valor de la viscosidad corregida (mu_w_p)") * 2.42
else:
    mu_w_a = mu_a
    mu_w_p = mu_p

Nusselt_a = float((mu_a/mu_w_a))
Nusselt_p = float((mu_p/mu_w_p))  

hi_a = float(0.027 * Re_a**0.8 * Prandtl_a**(1/3) * (Nusselt_a)**0.14 * (K_a/D_eq))
hi_p = float(0.027 * Re_p**0.8 * Prandtl_p**(1/3) * (Nusselt_p)**0.14 * (K_p/D_p))
hi_pc = float(hi_p * (dI/dE))
st.write("El valor de hia para el fluido en el anulo es de: ", hi_a)
st.write("El valor de hip corregido para el fluido en el tubo interno es de: ", hi_pc)

U_c = float((hi_pc * hi_a) / (hi_pc + hi_a))
st.write("El valor de la conductividad global (Uc) es de: ", U_c)
U_D = float(((1/U_c) + (Rd_prob))**-1)
st.write("El valor de la conductividad global con la resistencia de fouling (U_D) es de: ", U_D)

A = float(Q / (U_D * delta_T))
st.write("El valor del area de intercambio termico (A) es de: ", A)
L_N = float(A / SL)
st.write("El valor de la longitud necesaria para el intercambio termico (L_N) es de: ", L_N)
N = float(L_N / (2*L))
st.write("El número de tubos necesarios para el intercambio termico es de: ", N)
N_nuevo = st.number_input("Ingresa el número de tubos necesarios para el intercambio termico (N)")
A_calc = float(N_nuevo * (2*L) * SL)
st.write("El area calculada con el número de tubos necesario es de: ", A_calc)
U_calc = float(Q / (A_calc * delta_T))
st.write("El valor de la conductividad global calculada con el número de tubos necesario es de: ", U_calc)
Rd_calc = float((U_c - U_calc) / (U_calc * U_c))
st.write("El valor de la resistencia de fouling calculada con el número de tubos necesario es de: ", Rd_calc)

#==============================
st.header("Ecuaciones Adicionales")
#==============================

densidad_referencia = 62.5
g = 416923200

#Para el tubo interno (p)
ff_p = float(0.0035 + (0.264 / Re_p**0.42))
GE_p = st.number_input("Ingresa el valor de GE para el fluido en el tubo interno (GE_p)")
densidad_p = GE_p * densidad_referencia
st.write("La densidad del fluido en el tubo interno es de: ", densidad_p)
L_totp = float((1/numero_de_division_p) * (2 * L *N_nuevo))
st.write("La longitud total del tubo interno es de: ", L_totp)
delta_Fp = float((4 * ff_p * G_p**2 * L_totp) / (2 * g * densidad_p**2 * D_p))
st.write("La perdida de carga total para el fluido en el tubo interno es de: ", delta_Fp)
deltaP_p = float((delta_Fp * densidad_p)/144)
st.write("La perdida de presión total para el fluido en el tubo interno es de: ", deltaP_p)

#para el anulo (a)
D_a = float((DI - dE) / 12)
st.write("El diametro equivalente del anulo es de: ", D_a)
Re_corregido = float((D_a * G_a) / mu_a)
st.write("El número de Reynolds corregido para el fluido en el anulo es de: ", Re_corregido)
ff_a = float(0.0035 + (0.264 / Re_corregido**0.42))
st.write("El factor de fricción para el fluido en el anulo es de: ", ff_a)
GE_a = st.number_input("Ingresa el valor de GE para el fluido en el anulo (GE_a)")
densidad_a = GE_a * densidad_referencia
st.write("La densidad del fluido en el anulo es de: ", densidad_a)
L_tota = float((1/numero_de_divisiones_a) * (2 * L * N_nuevo))
st.write("La longitud total del anulo es de: ", L_tota)
delta_Fa = float((4 * ff_a * G_a**2 * L_tota) / (2 * g * densidad_a**2 * D_a))
st.write("La perdida de carga total para el fluido en el anulo es de: ", delta_Fa)
V_a = float(G_a / (3600 * densidad_a))
st.write("La velocidad del fluido en el anulo es de: ", V_a)
delta_F_Va = float(N_nuevo * (V_a**2 / (2*32.17)))
st.write("La perdida de carga total por velocidad para el fluido en el anulo es de: ", delta_F_Va)
deltaP_a = float((delta_Fa + delta_F_Va) * densidad_a / 144)
st.write("La perdida de presión total para el fluido en el anulo es de: ", deltaP_a)
