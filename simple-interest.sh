#!/bin/bash

# Script para calcular el interés simple
# Fórmula: I = P * r * t

echo "------------------------------------------"
echo "   Calculadora de Interés Simple (Bash)   "
echo "------------------------------------------"

# Solicitar el capital inicial
read -p "Ingrese el capital principal (P): " principal

# Solicitar la tasa de interés anual
read -p "Ingrese la tasa de interés anual % (r): " tasa_porcentaje

# Solicitar el tiempo en años
read -p "Ingrese el tiempo en años (t): " tiempo

# Realizar el cálculo
# Usamos 'bc' para manejar operaciones con decimales
tasa_decimal=$(echo "scale=4; $tasa_porcentaje / 100" | bc -l)
interes=$(echo "scale=2; $principal * $tasa_decimal * $tiempo" | bc -l)
monto_total=$(echo "scale=2; $principal + $interes" | bc -l)

echo "------------------------------------------"
echo "Resultados:"
echo "Interés simple generado: $interes"
echo "Monto total acumulado: $monto_total"
echo "------------------------------------------"
