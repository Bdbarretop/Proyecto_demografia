# -----------------------------------------------------------
# Dashboard Demográfico del Valle del Cauca - Censo 2018
# -----------------------------------------------------------

import streamlit as st
import pandas as pd
import altair as alt
import warnings
warnings.filterwarnings('ignore')

# -----------------------------------------------------------
# Configuración general de la página
# -----------------------------------------------------------
st.set_page_config(
    page_title="Análisis Demográfico del Valle del Cauca",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

    
# -----------------------------------------------------------
# Encabezado
# -----------------------------------------------------------
st.title("📊 Análisis Demográfico del Departamento del Valle del Cauca")
st.markdown("---")

# -----------------------------------------------------------
# Sidebar de navegación
# -----------------------------------------------------------
st.sidebar.title("🧭 Navegación")
section = st.sidebar.radio(
    "Selecciona una sección:",
    [
        "📋 Medidas de estructura",
        "💀 Mortalidad (2023)",
        "👶 Fecundidad (2023)",
        "🚶‍♂️ Migración (2018)"
    ]
)

with st.sidebar:
    st.markdown("<div style='margin-top: auto;'>", unsafe_allow_html=True)
    st.markdown("---")
    st.caption("**2025 - Dashboard Demográfico del Valle del Cauca**")
    st.caption(" Brayan David Barreto")
    st.caption("Demografía")
    st.caption("Universidad Santo Tomás de Aquino")
    st.caption("Fuente: DANE - Procesamiento propio")
    st.markdown("</div>", unsafe_allow_html=True)
# -----------------------------------------------------------
# SECCIÓN: Medidas de estructura - VALLE DEL CAUCA
# -----------------------------------------------------------
if section == "📋 Medidas de estructura":
    st.header("📊 Medidas de Estructura Poblacional - Valle del Cauca")
    
    # Pestañas para diferentes vistas - MODIFICADO PARA AGREGAR NUEVA PESTAÑA
    tab1, tab2, tab3 = st.tabs([
        "🏛️ Estructura por Edad y Sexo",
        "🗺️ Distribución Poblacional", 
        "📊 Índices de Estructura"  # NUEVA PESTAÑA
    ])
     # ---------------------------
    # PESTAÑA 1: Estructura por Edad y Sexo - CORREGIDA
    # ---------------------------
    with tab1:
        st.subheader("Estructura Poblacional por Grupos de Edad y Sexo")
        
        # Controles de selección simplificados
        col_sel1, col_sel2 = st.columns(2)
        with col_sel1:
            año_seleccionado = st.selectbox(
                "📅 Año:",
                ["2018", "2025"],
                key="selector_año"
            )
        with col_sel2:
            vista_sexo = st.selectbox(
                "👥 Vista:",
                ["Total", "Por Sexo", "Comparativa"],
                key="vista_sexo"
            )
        
        # Datos para 2018 y 2025
        if año_seleccionado == "2018":
            data_estructura = {
                "Grupo_Edad": ["Total", "0 a 4", "5 a 9", "10 a 14", "15 a 19", "20 a 24", "25 a 29", 
                            "30 a 34", "35 a 39", "40 a 44", "45 a 49", "50 a 54", "55 a 59", 
                            "60 a 64", "65 a 69", "70 a 74", "75 a 79", "80 a 84", "85 y más"],
                "Total": [3789874, 217172, 243519, 271616, 300093, 324147, 308447, 279863, 276955, 
                        244328, 245150, 247585, 220898, 184014, 141912, 105278, 77792, 53746, 47359],
                "Hombres": [1800614, 111269, 124419, 138549, 151474, 160436, 149790, 134472, 130517,
                        113428, 112325, 112604, 98939, 80733, 62532, 46106, 33169, 21802, 18050],
                "Mujeres": [1989260, 105903, 119100, 133067, 148619, 163711, 158657, 145391, 146438,
                        130900, 132825, 134981, 121959, 103281, 79380, 59172, 44623, 31944, 29309],
                "%_Total": [100.00, 5.73, 6.43, 7.17, 7.92, 8.55, 8.14, 7.38, 7.31, 6.45, 6.47, 
                        6.53, 5.83, 4.86, 3.74, 2.78, 2.05, 1.42, 1.25],
                "%_Hombres": [100.00, 6.18, 6.91, 7.69, 8.41, 8.91, 8.32, 7.47, 7.25, 6.30, 6.24,
                            6.25, 5.49, 4.48, 3.47, 2.56, 1.84, 1.21, 1.00],
                "%_Mujeres": [100.00, 5.32, 5.99, 6.69, 7.47, 8.23, 7.98, 7.31, 7.36, 6.58, 6.68,
                            6.79, 6.13, 5.19, 3.99, 2.97, 2.24, 1.61, 1.47]
            }
        else:  # 2025
            data_estructura = {
                "Grupo_Edad": ["Total", "0 a 4", "5 a 9", "10 a 14", "15 a 19", "20 a 24", "25 a 29",
                            "30 a 34", "35 a 39", "40 a 44", "45 a 49", "50 a 54", "55 a 59",
                            "60 a 64", "65 a 69", "70 a 74", "75 a 79", "80 a 84", "85 y más"],
                "Total": [4708393, 280297, 306630, 329031, 347972, 354315, 370581, 367106, 332043,
                        320531, 298282, 275358, 270285, 249698, 204426, 158451, 110680, 69872, 62835],
                "Hombres": [2239662, 143532, 156983, 168131, 176535, 177315, 180297, 177260, 157962,
                        150663, 138520, 126919, 123190, 110700, 87266, 66585, 45843, 28197, 23764],
                "Mujeres": [2468731, 136765, 149647, 160900, 171437, 177000, 190284, 189846, 174081,
                        169868, 159762, 148439, 147095, 138998, 117160, 91866, 64837, 41675, 39071],
                "%_Total": [100.00, 5.95, 6.51, 6.99, 7.39, 7.53, 7.87, 7.80, 7.05, 6.81, 6.34,
                        5.85, 5.74, 5.30, 4.34, 3.37, 2.35, 1.48, 1.33],
                "%_Hombres": [100.00, 6.41, 7.01, 7.51, 7.88, 7.92, 8.05, 7.91, 7.05, 6.73, 6.18,
                            5.67, 5.50, 4.94, 3.90, 2.97, 2.05, 1.26, 1.06],
                "%_Mujeres": [100.00, 5.54, 6.06, 6.52, 6.94, 7.17, 7.71, 7.69, 7.05, 6.88, 6.47,
                            6.01, 5.96, 5.63, 4.75, 3.72, 2.63, 1.69, 1.58]
            }
        
        df_estructura = pd.DataFrame(data_estructura)
        
        # --- VISTA TOTAL ---
        if vista_sexo == "Total":
            st.markdown(f"**📋 Distribución Poblacional Total - {año_seleccionado}**")
            df_display = df_estructura[["Grupo_Edad", "Total", "%_Total"]].copy()
            df_display.columns = ["Grupo de Edad", "Población", "% del Total"]
            df_display = df_display.round(2)
            st.dataframe(df_display, use_container_width=True, height=500)
            
            # RESUMEN DEBAJO DE LA TABLA
            st.markdown("**🎯 Indicadores Clave**")
            col1, col2, col3, col4 = st.columns(4)
            
            total_pob = df_estructura.loc[0, "Total"]
            youth = df_estructura.loc[1:3, "Total"].sum()
            working = df_estructura.loc[4:12, "Total"].sum()
            elderly = df_estructura.loc[13:18, "Total"].sum()
            
            with col1:
                st.metric("👥 Población Total", f"{total_pob:,}")
            with col2:
                st.metric("👶 0-14 años (Jóvenes)", f"{youth:,}", f"{youth/total_pob*100:.1f}%")
            with col3:
                st.metric("💼 15-59 años (Adultos)", f"{working:,}", f"{working/total_pob*100:.1f}%")
            with col4:
                st.metric("👴 60+ años (Adultos Mayores)", f"{elderly:,}", f"{elderly/total_pob*100:.1f}%")
            
            
        
        # --- VISTA POR SEXO ---
        elif vista_sexo == "Por Sexo":
            sexo_analizar = st.radio("Seleccionar sexo:", ["Hombres", "Mujeres"], horizontal=True, key="radio_sexo")
            
            st.markdown(f"**📋 Distribución de {sexo_analizar} - {año_seleccionado}**")
            df_display = df_estructura[["Grupo_Edad", sexo_analizar, f"%_{sexo_analizar}"]].copy()
            df_display.columns = ["Grupo de Edad", "Población", "% del Total"]
            df_display = df_display.round(2)
            st.dataframe(df_display, use_container_width=True, height=500)
            
            # RESUMEN DEBAJO DE LA TABLA
            st.markdown(f"**🎯 Indicadores {sexo_analizar}**")
            col1, col2, col3, col4 = st.columns(4)
            
            total_sexo = df_estructura.loc[0, sexo_analizar]
            youth_sexo = df_estructura.loc[1:3, sexo_analizar].sum()
            working_sexo = df_estructura.loc[4:12, sexo_analizar].sum()
            elderly_sexo = df_estructura.loc[13:18, sexo_analizar].sum()
            
            with col1:
                st.metric(f"👥 Total {sexo_analizar}", f"{total_sexo:,}")
            with col2:
                st.metric("👶 0-14 años", f"{youth_sexo:,}", f"{youth_sexo/total_sexo*100:.1f}%")
            with col3:
                st.metric("💼 15-59 años", f"{working_sexo:,}", f"{working_sexo/total_sexo*100:.1f}%")
            with col4:
                st.metric("👴 60+ años", f"{elderly_sexo:,}", f"{elderly_sexo/total_sexo*100:.1f}%")
            
            # Gráfico de distribución por edad
            df_chart = df_estructura[df_estructura["Grupo_Edad"] != "Total"].copy()
            
            chart_edad = alt.Chart(df_chart).mark_line(point=True, size=3).encode(
                x=alt.X('Grupo_Edad:N', title='Grupo de Edad', sort=None),
                y=alt.Y(f'%_{sexo_analizar}:Q', title='Porcentaje (%)', scale=alt.Scale(domain=[0, 10])),
                color=alt.value('#1f77b4' if sexo_analizar == 'Hombres' else '#ff7f0e'),
                tooltip=['Grupo_Edad', alt.Tooltip(f'%_{sexo_analizar}:Q', format='.2f', title='%')]
            ).properties(
                title=f'Distribución por Edad - {sexo_analizar} {año_seleccionado}',
                height=250
            )
            st.altair_chart(chart_edad, use_container_width=True)
            
            # Grupo modal
            idx_max = df_estructura[df_estructura["Grupo_Edad"] != "Total"][sexo_analizar].idxmax()
            grupo_modal = df_estructura.loc[idx_max, "Grupo_Edad"]
            pct_modal = df_estructura.loc[idx_max, f"%_{sexo_analizar}"]
            
            st.success(f"**🎯 Grupo Modal:** {grupo_modal} años ({pct_modal:.2f}%)")
        
        # --- VISTA COMPARATIVA ---
        else:  # Comparativa
            st.markdown(f"**⚖️ Comparación Hombres vs Mujeres - {año_seleccionado}**")
            
            # Tabla comparativa
            df_comp = df_estructura[["Grupo_Edad", "Hombres", "Mujeres", "%_Hombres", "%_Mujeres"]].copy()
            df_comp.columns = ["Grupo de Edad", "Hombres", "Mujeres", "% Hombres", "% Mujeres"]
            df_comp["Diferencia"] = df_comp["Hombres"] - df_comp["Mujeres"]
            df_comp = df_comp.round(2)
            st.dataframe(df_comp, use_container_width=True, height=500)
            
            # RESUMEN DEBAJO DE LA TABLA
            st.markdown("**📊 Resumen Comparativo**")
            col1, col2, col3, col4 = st.columns(4)
            
            total_h = df_estructura.loc[0, "Hombres"]
            total_m = df_estructura.loc[0, "Mujeres"]
            ind_masc = (total_h / total_m) * 100
            diferencia = total_m - total_h
            
            with col1:
                st.metric("👨 Hombres", f"{total_h:,}")
            with col2:
                st.metric("👩 Mujeres", f"{total_m:,}")
            with col3:
                st.metric("⚖️ Índice Masculinidad", f"{ind_masc:.2f}", 
                        help="Hombres por cada 100 mujeres")
            with col4:
                st.metric("➕ Diferencia", f"{diferencia:,}", "Más mujeres")
        
        # --- PIRÁMIDES POBLACIONALES ---
        st.markdown("---")
        st.subheader("📊 Pirámides Poblacionales")

        # Controles para pirámides
        col_p1, col_p2 = st.columns(2)
        with col_p1:
            año_piramide = st.radio(
                "Seleccionar año:",
                ["2018", "2025", "Ambos"],
                horizontal=True,
                key="año_piramide"
            )
        with col_p2:
            sexo_piramide = st.radio(
                "Seleccionar sexo:",
                ["Ambos", "Hombres", "Mujeres"],
                horizontal=True,
                key="sexo_piramide"
            )

        # Preparar datos para pirámides
        grupos_edad = ['85 y más', '80 a 84', '75 a 79', '70 a 74', '65 a 69', '60 a 64', 
                    '55 a 59', '50 a 54', '45 a 49', '40 a 44', '35 a 39', '30 a 34', 
                    '25 a 29', '20 a 24', '15 a 19', '10 a 14', '5 a 9', '0 a 4']

        # Datos 2018 (en porcentajes)
        piramide_2018 = pd.DataFrame({
            'Grupo_Edad': grupos_edad,
            'Hombres_2018': [1.25, 1.42, 2.05, 2.78, 3.74, 4.86, 5.83, 6.53, 6.47, 6.45, 7.31, 7.38, 8.14, 8.55, 7.92, 7.17, 6.43, 5.73],
            'Mujeres_2018': [1.47, 1.61, 2.24, 2.97, 3.99, 5.19, 6.13, 6.79, 6.68, 6.58, 7.36, 7.31, 7.98, 8.23, 7.47, 6.69, 5.99, 5.32]
        })

        # Datos 2025 (en porcentajes)
        piramide_2025 = pd.DataFrame({
            'Grupo_Edad': grupos_edad,
            'Hombres_2025': [1.33, 1.48, 2.35, 3.37, 4.34, 5.30, 5.74, 5.85, 6.34, 6.81, 7.05, 7.80, 7.87, 7.53, 7.39, 6.99, 6.51, 5.95],
            'Mujeres_2025': [1.58, 1.69, 2.63, 3.72, 4.75, 5.63, 5.96, 6.01, 6.47, 6.88, 7.05, 7.69, 7.71, 7.17, 6.94, 6.52, 6.06, 5.54]
        })

        # Combinar datos
        piramide_completa = pd.merge(piramide_2018, piramide_2025, on='Grupo_Edad')

        # Determinar qué datos mostrar según selección
        if año_piramide == "2018":
            variables = ['Hombres_2018', 'Mujeres_2018']
        elif año_piramide == "2025":
            variables = ['Hombres_2025', 'Mujeres_2025']
        else:  # Ambos años
            variables = ['Hombres_2018', 'Mujeres_2018', 'Hombres_2025', 'Mujeres_2025']

        # Filtrar por sexo si es necesario
        if sexo_piramide == "Hombres":
            variables = [v for v in variables if 'Hombres' in v]
        elif sexo_piramide == "Mujeres":
            variables = [v for v in variables if 'Mujeres' in v]

        # Preparar datos para el gráfico
        piramide_melted = piramide_completa.melt(id_vars=['Grupo_Edad'], 
                                            value_vars=variables,
                                            var_name='Año_Sexo', 
                                            value_name='Porcentaje')

        # Convertir a negativo los valores de hombres para la pirámide
        piramide_melted['Porcentaje_Piramide'] = piramide_melted.apply(
            lambda x: -x['Porcentaje'] if 'Hombres' in x['Año_Sexo'] else x['Porcentaje'], axis=1
        )

        # Colores armónicos
        colores_armonicos = {
            'Hombres_2018': '#3498db',  # Azul claro
            'Mujeres_2018': '#e74c3c',  # Rojo coral
            'Hombres_2025': '#2c3e50',  # Azul oscuro
            'Mujeres_2025': '#c0392b'   # Rojo oscuro
        }

        # Crear pirámide
        if año_piramide == "Ambos":
            # Vista superpuesta para ambos años
            datos_2018 = piramide_melted[piramide_melted['Año_Sexo'].str.contains('2018')]
            datos_2025 = piramide_melted[piramide_melted['Año_Sexo'].str.contains('2025')]
            
            # Pirámide 2018 (fondo)
            piramide_2018_chart = alt.Chart(datos_2018).mark_bar(opacity=0.6).encode(
                x=alt.X('Porcentaje_Piramide:Q', 
                    title='Porcentaje (%)',
                    axis=alt.Axis(format='.1f'),
                    scale=alt.Scale(domain=[-9, 9])),
                y=alt.Y('Grupo_Edad:N', title='Grupo de Edad', sort=grupos_edad),
                color=alt.Color('Año_Sexo:N', 
                            scale=alt.Scale(
                                domain=list(colores_armonicos.keys())[:2],
                                range=list(colores_armonicos.values())[:2]
                            ),
                            legend=alt.Legend(title="2018")),
                tooltip=['Grupo_Edad', 'Año_Sexo', alt.Tooltip('Porcentaje:Q', format='.2f', title='Porcentaje (%)')]
            )
            
            # Pirámide 2025 (frente)
            piramide_2025_chart = alt.Chart(datos_2025).mark_bar(opacity=0.8).encode(
                x=alt.X('Porcentaje_Piramide:Q', 
                    title='Porcentaje (%)',
                    axis=alt.Axis(format='.1f'),
                    scale=alt.Scale(domain=[-9, 9])),
                y=alt.Y('Grupo_Edad:N', title='Grupo de Edad', sort=grupos_edad),
                color=alt.Color('Año_Sexo:N', 
                            scale=alt.Scale(
                                domain=list(colores_armonicos.keys())[2:],
                                range=list(colores_armonicos.values())[2:]
                            ),
                            legend=alt.Legend(title="2025")),
                tooltip=['Grupo_Edad', 'Año_Sexo', alt.Tooltip('Porcentaje:Q', format='.2f', title='Porcentaje (%)')]
            )
            
            # Combinar gráficos
            piramide_final = piramide_2018_chart + piramide_2025_chart
            
        else:
            # Vista simple para un solo año
            piramide_final = alt.Chart(piramide_melted).mark_bar().encode(
                x=alt.X('Porcentaje_Piramide:Q', 
                    title='Porcentaje (%)',
                    axis=alt.Axis(format='.1f'),
                    scale=alt.Scale(domain=[-9, 9])),
                y=alt.Y('Grupo_Edad:N', title='Grupo de Edad', sort=grupos_edad),
                color=alt.Color('Año_Sexo:N', 
                            scale=alt.Scale(
                                domain=[v for v in colores_armonicos.keys() if v in variables],
                                range=[colores_armonicos[v] for v in colores_armonicos.keys() if v in variables]
                            ),
                            legend=alt.Legend(title=f"{año_piramide}")),
                tooltip=['Grupo_Edad', 'Año_Sexo', alt.Tooltip('Porcentaje:Q', format='.2f', title='Porcentaje (%)')]
            )

        piramide_final = piramide_final.properties(
            width=600,
            height=500,
            title=f'Pirámide Poblacional - {año_piramide}'
        ).configure_axis(
            grid=False
        )

        st.altair_chart(piramide_final, use_container_width=True)
    # ---------------------------
    # PESTAÑA 2: Distribución Geográfica
    # ---------------------------

    with tab2:
        st.subheader("Distribución Poblacional por Área Geográfica")
        
        # Selector de año para distribución geográfica
        col1, col2 = st.columns([1, 4])
        with col1:
            año_geo = st.selectbox(
                "Seleccionar año:",
                ["2018", "2023"],
                key="selector_geo"
            )
        
        if año_geo == "2018":
            data_geografica = {
                "Área": ["Total", "Cabecera", "Centro Poblado", "Rural Disperso"],
                "Total": [3789874, 3242187, 334019, 213668],
                "Hombres": [1800614, 1522399, 164771, 113444],
                "Mujeres": [1989260, 1719788, 169248, 100224],
                "%_Total": [100.0, 85.5, 8.8, 5.6],
                "%_Hombres": [100.0, 84.6, 9.2, 6.3],
                "%_Mujeres": [100.0, 86.4, 8.5, 5.0]
            }
        else:  # 2023
            data_geografica = {
                "Área": ["Total", "Cabecera", "Centro Poblado y Rural Disperso"],
                "Total": [4708393, 3999597, 708796],
                "Hombres": [2239662, 1879231, 360431],
                "Mujeres": [2468731, 2120366, 348365],
                "%_Total": [100.0, 85.0, 15.0],
                "%_Hombres": [100.0, 83.9, 16.1],
                "%_Mujeres": [100.0, 85.9, 14.1]
            }
        
        df_geo = pd.DataFrame(data_geografica)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown(f"**📊 Distribución por Área - {año_geo}**")
            st.dataframe(df_geo, use_container_width=True)
        
        with col2:
            # Gráfico de torta
            if año_geo == "2018":
                pie_data = pd.DataFrame({
                    'Área': ['Cabecera', 'Centro Poblado', 'Rural Disperso'],
                    'Población': [3242187, 334019, 213668],
                    'Porcentaje': [85.5, 8.8, 5.6]
                })
            else:
                pie_data = pd.DataFrame({
                    'Área': ['Cabecera', 'Centro Poblado y Rural Disperso'],
                    'Población': [3999597, 708796],
                    'Porcentaje': [85.0, 15.0]
                })
            
            pie_chart = alt.Chart(pie_data).mark_arc().encode(
                theta=alt.Theta(field="Población", type="quantitative"),
                color=alt.Color(field="Área", type="nominal", 
                            scale=alt.Scale(scheme='category10')),
                tooltip=['Área', 'Población', alt.Tooltip('Porcentaje:Q', format='.1f', title='Porcentaje (%)')]
            ).properties(
                width=400,
                height=300,
                title=f'Distribución Poblacional por Área - {año_geo}'
            )
            st.altair_chart(pie_chart, use_container_width=True)
        
        # Información de densidad poblacional
        st.markdown("---")
        st.subheader("🏙️ Densidad Poblacional")
        
        col_d1, col_d2 = st.columns(2)
        
        with col_d1:
            st.markdown("**2018**")
            st.metric(
                label="Densidad Poblacional",
                value="171,18",
                delta="41,49",
                delta_color="normal",
                help="personas por km²"
            )
            st.info("**Interpretación:** La densidad poblacional censal del Valle del Cauca fue de 171,18 personas por km² en el 2018.")
        
        with col_d2:
            st.markdown("**2025**")
            st.metric(
                label="Densidad Poblacional",
                value="212,67",
                help="personas por km²"
            )
            st.info("**Interpretación:** Se estima que para el año 2025 la densidad poblacional del Valle del Cauca será de 212,67 personas por km².")    
        # ---------------------------
    
    # ---------------------------
    # PESTAÑA 3: Índices de Estructura - NUEVA PESTAÑA
    # ---------------------------

    with tab3:
        st.subheader("📊 Índices de Estructura Poblacional")
        
        # Selector de vista
        vista_indices = st.radio(
            "Seleccionar vista:",
            ["🏛️ Vista 2018", "🏛️ Vista 2025", "📈 Vista Comparativa"],
            horizontal=True,
            key="vista_indices"
        )
        
        if vista_indices == "🏛️ Vista 2018":
            st.markdown("### 📊 Indicadores de Estructura - Año 2018")
            
            col1, col2, col3, col4, col5 = st.columns(5)
            
            with col1:
                st.metric(
                    label="Dependencia Demográfica",
                    value="54,85",
                    help="Por 100 personas activas"
                )
                st.info("**Interpretación:** En el Valle del Cauca, para el año 2018, por cada 100 personas en edad potencialmente activa (15 a 59 años), había 54,85 personas en edades dependientes (0 a 14 años o 60 años y más).")
            
            with col2:
                st.metric(
                    label="Dependencia Juvenil", 
                    value="29,92",
                    help="Por 100 personas activas"
                )
                st.info("**Interpretación:** En el Valle del Cauca, para el año 2018, por cada 100 personas en edad potencialmente activa (15 a 59 años), había 29,92 personas de 0 a 14 años.")
            
            with col3:
                st.metric(
                    label="Dependencia Senil",
                    value="24,93",
                    help="Por 100 personas activas"
                )
                st.info("**Interpretación:** En el Valle del Cauca, para el año 2018, por cada 100 personas en edad potencialmente activa (15 a 59 años), había 24,93 personas de 60 años o más.")
            
            with col4:
                st.metric(
                    label="Índice de Envejecimiento",
                    value="83,31",
                    help="Por 100 jóvenes"
                )
                st.info("**Interpretación:** En el Valle del Cauca, para el año 2018, por cada 100 personas menores de 15 años, había 83,31 personas de 60 años y más.")
            
            with col5:
                st.metric(
                    label="Índice de Masculinidad",
                    value="90,52",
                    help="Hombres por 100 mujeres"
                )
                st.info("**Interpretación:** En el Valle del Cauca, para el año 2018, por cada 100 mujeres había 90,51 hombres.")
        
        elif vista_indices == "🏛️ Vista 2025":
            st.markdown("### 📊 Indicadores de Estructura - Año 2025")
            
            col1, col2, col3, col4, col5 = st.columns(5)
            
            with col1:
                st.metric(
                    label="Dependencia Demográfica",
                    value="60,34",
                    delta="+5,49",
                    help="Por 100 personas activas"
                )
                st.info("**Interpretación:** En el Valle del Cauca se estima que, para el 2025, por cada 100 personas en edad potencialmente activa (15 a 59 años), habrá 60,34 personas en edades dependientes (0 a 14 años o 60 años y más).")
            
            with col2:
                st.metric(
                    label="Dependencia Juvenil",
                    value="31,19",
                    delta="+1,27", 
                    help="Por 100 personas activas"
                )
                st.info("**Interpretación:** En el Valle del Cauca se estima que, para el 2025, por cada 100 personas en edad potencialmente activa (15 a 59 años), habrá 31,19 personas de 0 a 14 años.")
            
            with col3:
                st.metric(
                    label="Dependencia Senil",
                    value="29,15",
                    delta="+4,22",
                    help="Por 100 personas activas"
                )
                st.info("**Interpretación:** En el Valle del Cauca se estima que, para el 2025, por cada 100 personas en edad potencialmente activa (15 a 59 años), habrá 29,15 personas de 60 años o más.")
            
            with col4:
                st.metric(
                    label="Índice de Envejecimiento",
                    value="93,45",
                    delta="+10,14",
                    help="Por 100 jóvenes"
                )
                st.info("**Interpretación:** En el Valle del Cauca se estima que, para el 2025, por cada 100 personas menores de 15 años, habrá 93,45 personas de 60 años y más.")
            
            with col5:
                st.metric(
                    label="Índice de Masculinidad",
                    value="90,72",
                    delta="+0,20",
                    help="Hombres por 100 mujeres"
                )
                st.info("**Interpretación:** Se estima que el Valle del Cauca tendrá por cada 100 mujeres, 90,72 hombres para el 2025.")
        
        else:  # Vista Comparativa
            st.markdown("### 📈 Evolución Comparativa 2018-2025")
            
            # Datos para la tabla comparativa
            comparativa_data = {
                "Índice": [
                    "Índice de Dependencia Demográfica",
                    "Índice de Dependencia Juvenil",
                    "Índice de Dependencia Senil", 
                    "Índice de Envejecimiento",
                    "Índice de Masculinidad"
                ],
                "2018": ["54,85", "29,92", "24,93", "83,31", "90,52"],
                "2025": ["60,34", "31,19", "29,15", "93,45", "90,72"],
                "Cambio": ["+5,49", "+1,27", "+4,22", "+10,14", "+0,20"]
            }
            
            df_comparativa = pd.DataFrame(comparativa_data)
            st.dataframe(df_comparativa, use_container_width=True)
            
            st.markdown("---")
            st.subheader("🎯 Cambios Numéricos 2018-2025")
            
            col1, col2, col3, col4, col5 = st.columns(5)
            
            with col1:
                st.metric(
                    label="Dependencia Demográfica",
                    value="+5,49",
                    help="Cambio absoluto"
                )
            
            with col2:
                st.metric(
                    label="Dependencia Juvenil",
                    value="+1,27",
                    help="Cambio absoluto"
                )
            
            with col3:
                st.metric(
                    label="Dependencia Senil", 
                    value="+4,22",
                    help="Cambio absoluto"
                )
            
            with col4:
                st.metric(
                    label="Envejecimiento",
                    value="+10,14",
                    help="Cambio absoluto"
                )
            
            with col5:
                st.metric(
                    label="Masculinidad",
                    value="+0,20",
                    help="Cambio absoluto"
                )

        # Footer de la sección
        st.markdown("---")
        st.caption("Fuente: Procesamiento de datos censales DANE | Elaboración propia")

# -----------------------------------------------------------
# SECCIÓN: Mortalidad (2023) - VALLE DEL CAUCA
# -----------------------------------------------------------
elif section == "💀 Mortalidad (2023)":
    st.header("💀 Análisis de Mortalidad - Valle del Cauca 2023")
    
    # Pestañas según la estructura solicitada
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "1️⃣ Tasa Bruta de Mortalidad",
        "2️⃣ Tasas Específicas por Edad",
        "3️⃣ Tasas Estandarizadas", 
        "4️⃣ Mortalidad Infantil",
        "5️⃣ Causas de Mortalidad",
        "6️⃣ Tabla de Mortalidad",
        "7️⃣ Comparación Nacional"
    ])
    
    # ---------------------------
    # PESTAÑA 1: Tasa Bruta de Mortalidad
    # ---------------------------
    with tab1:
        st.subheader("1. Tasa Bruta de Mortalidad")
        
        col1, col2 = st.columns([1.2, 1])
        
        with col1:
            # Datos TBM REALES
            data_tbm_valle = {
                "Indicador": ["Defunciones 2023", "Población 2023", "TBM 2023"],
                "Hombres": [15863, 2222937, 7.14],
                "Mujeres": [13441, 2450458, 5.49],
                "Total": [29304, 4673395, 6.27]
            }
            df_tbm = pd.DataFrame(data_tbm_valle)
            st.dataframe(df_tbm, use_container_width=True)
        
        with col2:
            # Gráfico de barras TBM
            df_tbm_chart = df_tbm[df_tbm["Indicador"] == "TBM 2023"].melt(
                id_vars=["Indicador"], 
                var_name="Sexo", 
                value_name="TBM"
            )
            
            chart_tbm = alt.Chart(df_tbm_chart).mark_bar().encode(
                x=alt.X("Sexo:N", title="Sexo"),
                y=alt.Y("TBM:Q", title="Tasa Bruta de Mortalidad"),
                color=alt.Color("Sexo:N", scale=alt.Scale(
                    domain=["Hombres", "Mujeres", "Total"],
                    range=["#1f2eb4", "#eb0eff", "#009e73"]
                )),
                tooltip=["Sexo", "TBM"]
            ).properties(
                title="Tasa Bruta de Mortalidad por Sexo",
                height=300
            )
            st.altair_chart(chart_tbm, use_container_width=True)
            
            st.info("""
            **📌 Interpretación:** 
            - **Hombres:** 7.14 defunciones por cada mil habitantes hombres
            - **Mujeres:** 5.49 defunciones por cada mil habitantes mujeres
            - **Total:** 6.27 defunciones por cada mil habitantes totales
            
            La TBM en hombres es **30% mayor** que en mujeres, 
            reflejando diferencias significativas en patrones 
            de mortalidad por género.
            """)
    
    # ---------------------------
    # PESTAÑA 2: Tasas Específicas por Edad
    # ---------------------------
    with tab2:
        st.subheader("2. Tasas Específicas de Mortalidad por Edad")
        
        # Selector de sexo
        col1, col2 = st.columns([1, 4])
        with col1:
            sexo_seleccionado = st.selectbox(
                "Seleccionar sexo:",
                ["Total", "Hombres", "Mujeres"],
                key="tasas_edad"
            )
        
        # Datos de TEM REALES - actualizados con los valores de la tabla
        data_tasas_valle = {
            "Grupo_Edad": ["0", "1", "2-4", "5-9", "10-14", "15-19", "20-24", "25-29", "30-34", 
                        "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", 
                        "75-79", "80-84", "85 y más"],
            "Hombres": [12.1205621, 0.44684288, 0.23080728, 0.18013653, 0.2839082, 1.7763473, 
                    3.32791666, 3.55168187, 3.589114, 3.34798211, 3.36458721, 3.62220411, 
                    4.642139, 6.63930271, 10.4504436, 17.0163535, 25.7107855, 38.0453752, 
                    64.9516979, 128.22996],
            "Mujeres": [7.9485027, 0.5047046, 0.1961327, 0.1498567, 0.2112277, 0.4922584, 
                    0.5266565, 0.7821565, 0.9138580, 1.0455274, 1.4867412, 2.1266464, 
                    2.7640247, 4.1990015, 6.4613930, 9.4385286, 14.2999941, 24.6413755, 
                    43.9833201, 121.2598425],
            "Total": [10.0791542, 0.47508446, 0.2138905, 0.16535811, 0.2483084, 1.14314101, 
                    1.91726478, 2.13206029, 2.20011128, 2.13840709, 2.36491193, 2.82006515, 
                    3.62919275, 5.30554134, 8.22092477, 12.6707206, 19.1496267, 30.2341839, 
                    52.4579981, 123.890864]
        }
        df_tasas = pd.DataFrame(data_tasas_valle)
        
        # TABLA - Mostrar la tabla completa
        st.markdown("**📊 Tasas Específicas de Mortalidad por Edad (por 1000 habitantes)**")
        df_display = df_tasas.copy()
        df_display.columns = ["Grupo de Edad", "Hombres", "Mujeres", "Total"]
        st.dataframe(df_display, use_container_width=True, height=400)
        
        st.caption("**Fuente:** Elaboración propia, basado en datos recogidos del DANE (Proyecciones Poblacionales y Estadísticas Vitales)")
        
        # GRÁFICO CON LAS TRES CURVAS JUNTAS
        st.markdown("**📈 Comparativa de Tasas de Mortalidad por Grupos de Edad**")
        
        # Preparar datos para el gráfico comparativo
        df_melted = df_tasas.melt(id_vars=['Grupo_Edad'], 
                                value_vars=['Hombres', 'Mujeres', 'Total'],
                                var_name='Sexo', 
                                value_name='Tasa')
        
        # Crear gráfico con las tres curvas
        chart_comparativo = alt.Chart(df_melted).mark_line(point=True, size=2.5).encode(
            x=alt.X('Grupo_Edad:N', title='Grupo de Edad', sort=None),
            y=alt.Y('Tasa:Q', title='Tasa por 1000 habitantes', scale=alt.Scale(type='log')),
            color=alt.Color('Sexo:N', 
                        scale=alt.Scale(domain=['Hombres', 'Mujeres', 'Total'],
                                        range=['#1f77b4', '#ff7f0e', '#2ca02c']),
                        legend=alt.Legend(title="Sexo")),
            strokeDash=alt.StrokeDash('Sexo:N',
                                    scale=alt.Scale(domain=['Hombres', 'Mujeres', 'Total'],
                                                    range=[[1, 0], [5, 5], [3, 3]])),
            tooltip=['Grupo_Edad', 'Sexo', alt.Tooltip('Tasa:Q', format='.2f')]
        ).properties(
            height=400,
            title='Tasas Específicas de Mortalidad por Edad y Sexo'
        )
        
        st.altair_chart(chart_comparativo, use_container_width=True)
        
        # INTERPRETACIÓN
        st.info("""
        **📌 Interpretación:** 
        Las tasas representan el número de defunciones por cada 1000 habitantes del grupo etario 
        analizado durante el año 2023.
        
        **Ejemplos:**
        - **Grupo 0 años (Hombres):** 12.12 defunciones por cada 1000 niños menores de 1 año
        - **Grupo 20-24 años (Hombres):** 3.33 defunciones por cada 1000 hombres de 20-24 años
        - **Grupo 85+ años (Total):** 123.89 defunciones por cada 1000 adultos mayores de 85+ años
        
        **Patrón observado:** Curva en forma de "U" con alta mortalidad infantil, mínima en 
        edades jóvenes y aumento progresivo en edades avanzadas.
        """)
    # ---------------------------
    # PESTAÑA 3: Tasas Estandarizadas
    # ---------------------------

    with tab3:
        st.subheader("3. Tasas Estandarizadas Directas")
        
        # Gráfico comparativo
        comparativa_data = {
            "Región": ["Valle del Cauca", "Bogotá"],
            "TBM Estandarizada": [5.34, 4.53],
            "Defunciones Esperadas": ["27,443", "23,256"],
            "Interpretación": ["5.34", "4.53"]
        }
        df_comparativa = pd.DataFrame(comparativa_data)
        
        col1, col2 = st.columns([1.5, 1])  # Cambié la proporción a 2:1 para gráfico más ancho
        
        with col1:
            chart_estandar = alt.Chart(df_comparativa).mark_bar(size=40).encode(  # Aumenté el tamaño de las barras
                x=alt.X('Región:N', title='Región'),
                y=alt.Y('TBM Estandarizada:Q', title='TBM Estandarizada', scale=alt.Scale(domain=[0, 6])),  # Fijé el dominio del eje Y
                color=alt.Color('Región:N', scale=alt.Scale(
                    domain=['Valle del Cauca', 'Bogotá'],
                    range=['#1f2eb4', '#009e73']
                )),
                tooltip=['Región', 'TBM Estandarizada']
            ).properties(
                title='Comparación de TBM Estandarizada',
                height=300  # Aumenté la altura
            )
            st.altair_chart(chart_estandar, use_container_width=True)
        
        with col2:
            st.metric("Diferencia", "+0.81")
            
            st.success("""
            **✅ Conclusión:** 
            El Valle del Cauca presenta **mayores defunciones por habitante** que Bogotá 
            cuando se compara con el fenómeno de la mortalidad a nivel nacional.
            """)
    
    # ---------------------------
    # PESTAÑA 4: Mortalidad Infantil
    # ---------------------------
    with tab4:
        st.subheader("4. Mortalidad Infantil y de la Niñez")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Tasa Mortalidad Infantil", "10.08", "Por 1000 nacimientos")
            st.metric("Defunciones <1 año", "368", "Total 2023")
            st.metric("Nacimientos", "36,514", "Base de cálculo")
            
        with col2:
            st.metric("Tasa Mortalidad <5 años", "11.86", "Por 1000 nacimientos")
            st.metric("Defunciones <5 años", "433", "Incluye 1-4 años")
            st.metric("Tasa Poblacional <5 años", "1.49", "Por 1000 niños <5 años")
            
        with col3:
            st.metric("Mortalidad Neonatal", "65.76%", "Del total infantil")
            st.metric("Periodo Neonatal Precoz", "42.4%", "<7 días del total")
            st.metric("Hombres vs Mujeres", "226 vs 142", "59% más en hombres")
        
        # NUEVAS MÉTRICAS DE MORTALIDAD MATERNA
        st.markdown("---")
        st.subheader("Mortalidad Materna")
        
        col4, col5 = st.columns(2)
        
        with col4:
            st.metric(
                "Razón de Mortalidad Materna (RMM)", 
                "52.03", 
                "Por 100,000 nacimientos"
            )
            
        with col5:
            st.metric(
                "Tasa de Mortalidad Materna (TMM)", 
                "0.015", 
                "Por 1,000 mujeres en edad fértil"
            )
        
        st.info("""
        **📌 Interpretación Mortalidad Materna:**
        - **RMM:** 52.03 defunciones maternas por cada 100,000 nacimientos
        - **TMM:** 0.015 defunciones maternas por cada 1,000 mujeres en edad fértil
        - Las defunciones maternas incluyen causas asociadas al embarazo, parto o puerperio
        """)
        
        # Gráfico de distribución por período - Datos del documento
        distrib_data = pd.DataFrame({
            'Periodo': ['<1 hora', '1-23 horas', '1-6 días', '7-27 días', '1-5 meses', '6-11 meses'],
            'Defunciones': [15, 47, 94, 84, 90, 36],
            'Porcentaje': [4.1, 12.8, 25.5, 22.8, 24.5, 9.8],
            'Tipo': ['Neonatal Precoz', 'Neonatal Precoz', 'Neonatal Precoz', 'Neonatal Tardía', 'Postneonatal', 'Postneonatal']
        })
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            chart_distrib = alt.Chart(distrib_data).mark_bar().encode(
                x=alt.X('Periodo:N', title='Periodo de Edad', sort=None),
                y=alt.Y('Defunciones:Q', title='Número de Defunciones'),
                color=alt.Color('Tipo:N', 
                            scale=alt.Scale(domain=['Neonatal Precoz', 'Neonatal Tardía', 'Postneonatal'],
                                            range=['#ff6b6b', '#ffa726', '#42a5f5']),
                            legend=alt.Legend(title="Tipo de Mortalidad")),
                tooltip=['Periodo', 'Defunciones', 'Porcentaje', 'Tipo']
            ).properties(
                height=350,
                title='Distribución de Mortalidad Infantil por Periodo de Edad - Valle del Cauca 2023'
            )
            st.altair_chart(chart_distrib, use_container_width=True)
        
        with col2:
            st.info("""
            **📌 Interpretación Mortalidad Infantil:**
            
            - **Tasa Infantil:** 10.08 defunciones por cada 1000 nacimientos
            - **Tasa <5 años:** 11.86 defunciones por cada 1000 nacimientos  
            - **Tasa Poblacional:** 1.49 defunciones por cada 1000 niños <5 años
            
            **Períodos críticos:**
            - 1 día a 5 meses: 73.37% del total
            - Neonatal (0-27 días): 65.76% del total
            - Neonatal Precoz (<7 días): 42.4% del total
            """)
        
        # Principales causas de mortalidad infantil
        st.markdown("**🩺 Principales Causas de Mortalidad Infantil**")
        
        causas_data = pd.DataFrame({
            'Causa': [
                'Malformaciones congénitas', 
                'Trastornos respiratorios perinatales',
                'Complicaciones gestacionales',
                'Sepsis bacteriana',
                'Asfixia perinatal'
            ],
            'Porcentaje': [28.5, 18.3, 15.2, 12.1, 9.8]
        })
        
        chart_causas = alt.Chart(causas_data).mark_bar().encode(
            x=alt.X('Porcentaje:Q', title='Porcentaje (%)'),
            y=alt.Y('Causa:N', title='Causa', sort='-x'),
            color=alt.Color('Porcentaje:Q', scale=alt.Scale(scheme='reds')),
            tooltip=['Causa', 'Porcentaje']
        ).properties(
            height=300,
            title='Principales Causas de Mortalidad Infantil - Valle del Cauca 2023'
        )
        
        st.altair_chart(chart_causas, use_container_width=True)
        
        st.success("""
        **🔍 Hallazgos Clave:**
        - Los períodos más críticos son entre 1 día y 5 meses de edad (73.37% acumulado)
        - La mortalidad neonatal representa casi dos tercios del total infantil
        - Los trastornos respiratorios del período perinatal son causa común en todos los grupos
        - Los hombres presentan 59% más mortalidad infantil que las mujeres
        - La mortalidad materna muestra 52 defunciones por cada 100,000 nacimientos
        """)
    
    
    # ---------------------------
    # PESTAÑA 5: Causas de Mortalidad
    # ---------------------------
    with tab5:
        st.subheader("5. Causas de Mortalidad - Análisis por Grupos de Edad")
        
        # Filtro por grupo de edad CON DATOS REALES actualizados
        grupo_edad = st.selectbox(
            "Seleccionar grupo de edad:",
            ["TODAS LAS EDADES", "Menores de 1 año", "1-4 años", "5-14 años", "15-24 años", 
            "25-59 años", "60 años y más"],
            key="causas_edad"
        )
        
        # Datos de causas por grupo de edad ACTUALIZADOS con información completa
        causas_por_edad = {
            "TODAS LAS EDADES": [
                {"Causa": "Enfermedades isquémicas del corazón", "Porcentaje": 19.09, "Total": 5594, "Tasa": 1.197},
                {"Causa": "Enfermedades cerebrovasculares", "Porcentaje": 8.16, "Total": 2390, "Tasa": 0.511},
                {"Causa": "Agresiones (homicidios)", "Porcentaje": 7.57, "Total": 2217, "Tasa": 0.474},
                {"Causa": "Enfermedades crónicas vías respiratorias", "Porcentaje": 4.79, "Total": 1404, "Tasa": 0.300},
                {"Causa": "Enfermedades del sistema nervioso", "Porcentaje": 3.42, "Total": 1002, "Tasa": 0.214},
                {"Causa": "Enfermedades del sistema digestivo", "Porcentaje": 3.40, "Total": 997, "Tasa": 0.213},
                {"Causa": "Tumores digestivos", "Porcentaje": 3.26, "Total": 954, "Tasa": 0.204}
            ],
            "Menores de 1 año": [
                {"Causa": "Malformaciones congénitas", "Porcentaje": 27.17, "Total": 100, "Tasa": ""},
                {"Causa": "Trastornos respiratorios perinatal", "Porcentaje": 18.75, "Total": 69, "Tasa": ""},
                {"Causa": "Afecciones período perinatal", "Porcentaje": 13.32, "Total": 49, "Tasa": ""},
                {"Causa": "Complicaciones obstétricas", "Porcentaje": 9.24, "Total": 34, "Tasa": ""},
                {"Causa": "Infecciones respiratorias agudas", "Porcentaje": 5.98, "Total": 22, "Tasa": ""}
            ],
            "1-4 años": [
                {"Causa": "Malformaciones congénitas", "Porcentaje": 25.87, "Total": 112, "Tasa": ""},
                {"Causa": "Trastornos respiratorios perinatal", "Porcentaje": 15.94, "Total": 69, "Tasa": ""},
                {"Causa": "Afecciones período perinatal", "Porcentaje": 11.78, "Total": 51, "Tasa": ""},
                {"Causa": "Complicaciones obstétricas", "Porcentaje": 7.85, "Total": 34, "Tasa": ""},
                {"Causa": "Infecciones respiratorias agudas", "Porcentaje": 6.93, "Total": 30, "Tasa": ""}
            ],
            "5-14 años": [
                {"Causa": "Agresiones (homicidios)", "Porcentaje": 10.29, "Total": 14, "Tasa": ""},
                {"Causa": "Enfermedades del sistema nervioso", "Porcentaje": 8.82, "Total": 12, "Tasa": ""},
                {"Causa": "Accidentes transporte terrestre", "Porcentaje": 7.35, "Total": 10, "Tasa": ""},
                {"Causa": "Enfermedades cardiopulmonares", "Porcentaje": 7.35, "Total": 10, "Tasa": ""},
                {"Causa": "Infecciones respiratorias agudas", "Porcentaje": 7.35, "Total": 10, "Tasa": ""}
            ],
            "15-24 años": [
                {"Causa": "Agresiones (homicidios)", "Porcentaje": 55.87, "Total": 614, "Tasa": ""},
                {"Causa": "Accidentes transporte terrestre", "Porcentaje": 14.92, "Total": 164, "Tasa": ""},
                {"Causa": "Suicidios", "Porcentaje": 4.19, "Total": 46, "Tasa": ""},
                {"Causa": "Enfermedades sistema nervioso", "Porcentaje": 3.00, "Total": 33, "Tasa": ""},
                {"Causa": "VIH-SIDA", "Porcentaje": 1.82, "Total": 20, "Tasa": ""}
            ],
            "25-59 años": [
                {"Causa": "Signos y síntomas mal definidos", "Porcentaje": 23.70, "Total": 1484, "Tasa": ""},
                {"Causa": "Enfermedades isquémicas corazón", "Porcentaje": 8.70, "Total": 545, "Tasa": ""},
                {"Causa": "Accidentes transporte terrestre", "Porcentaje": 6.42, "Total": 402, "Tasa": ""},
                {"Causa": "VIH-SIDA", "Porcentaje": 3.96, "Total": 248, "Tasa": ""},
                {"Causa": "Enfermedades cerebrovasculares", "Porcentaje": 3.70, "Total": 232, "Tasa": ""}
            ],
            "60 años y más": [
                {"Causa": "Enfermedades isquémicas corazón", "Porcentaje": 23.57, "Total": 5037, "Tasa": ""},
                {"Causa": "Enfermedades cerebrovasculares", "Porcentaje": 10.04, "Total": 2146, "Tasa": ""},
                {"Causa": "Enfermedades vías respiratorias", "Porcentaje": 6.24, "Total": 1334, "Tasa": ""},
                {"Causa": "Enfermedades sistema digestivo", "Porcentaje": 3.86, "Total": 824, "Tasa": ""},
                {"Causa": "Enfermedades sistema nervioso", "Porcentaje": 3.78, "Total": 807, "Tasa": ""}
            ]
        }
        
        # Obtener datos para el grupo seleccionado
        datos_causas = causas_por_edad.get(grupo_edad, causas_por_edad["TODAS LAS EDADES"])
        df_causas = pd.DataFrame(datos_causas)
        
        col1, col2 = st.columns([1.5, 1])
        
        with col1:
            # Gráfico de barras horizontal
            chart_causas = alt.Chart(df_causas).mark_bar().encode(
                x=alt.X('Porcentaje:Q', title='Porcentaje (%)'),
                y=alt.Y('Causa:N', title='Causa', sort='-x'),
                color=alt.Color('Porcentaje:Q', scale=alt.Scale(scheme='reds')),
                tooltip=['Causa', 'Porcentaje', 'Total']
            ).properties(
                height=400,
                title=f'Principales Causas de Mortalidad - {grupo_edad}'
            )
            st.altair_chart(chart_causas, use_container_width=True)
        
        with col2:
            st.markdown("**📋 Análisis del Grupo**")
            
            # Total de defunciones por grupo (actualizados con datos reales)
            totales_grupo = {
                "TODAS LAS EDADES": 29304,
                "Menores de 1 año": 368,
                "1-4 años": 433,
                "5-14 años": 136,
                "15-24 años": 1099,
                "25-59 años": 6262,
                "60 años y más": 21374
            }
            
            total_grupo = totales_grupo[grupo_edad]
            st.metric(f"Defunciones {grupo_edad}", f"{total_grupo:,}")
            
            if grupo_edad == "TODAS LAS EDADES":
                st.info("""
                **🏥 Patrón General:**
                - **20%** enfermedades isquémicas
                - **8%** enfermedades cerebrovasculares  
                - **8%** homicidios
                - Por cada 1000 habitantes: 1.19 fallecimientos por enfermedades isquémicas
                """)
            elif grupo_edad == "Menores de 1 año":
                st.error("""
                **👶 Mortalidad Infantil:**
                - **27%** malformaciones congénitas
                - **19%** trastornos respiratorios perinatales
                - **13%** afecciones perinatales
                - Período neonatal: 65.76% del total
                """)
            elif grupo_edad == "1-4 años":
                st.error("""
                **🧒 Primera Infancia:**
                - **26%** malformaciones congénitas
                - **16%** trastornos respiratorios
                - **12%** afecciones perinatales
                - Continuación patrón mortalidad infantil
                """)
            elif grupo_edad == "5-14 años":
                st.warning("""
                **🎒 Edad Escolar:**
                - **10%** homicidios
                - **9%** enfermedades neurológicas
                - **7%** accidentes tránsito
                - Transición hacia causas externas
                """)
            elif grupo_edad == "15-24 años":
                st.error("""
                **⚠️ Jóvenes - ALERTA:**
                - **56%** homicidios (más del 50%)
                - **15%** accidentes tránsito
                - **4%** suicidios
                - Causas violentas predominantes
                """)
            elif grupo_edad == "25-59 años":
                st.warning("""
                **👨‍💼 Adultos:**
                - **24%** signos mal definidos
                - **9%** enfermedades cardíacas
                - **6%** accidentes tránsito
                - Déficit en diagnósticos
                """)
            elif grupo_edad == "60 años y más":
                st.info("""
                **👵 Adultos Mayores:**
                - **24%** enfermedades cardíacas
                - **10%** cerebrovasculares
                - **6%** respiratorias crónicas
                - Enfermedades crónicas predominan
                """)
            
            # Mostrar tasa específica si está disponible
            if grupo_edad == "TODAS LAS EDADES" and len(datos_causas) > 0:
                st.metric("Tasa Principal", f"{datos_causas[0]['Tasa']}", "Por 1000 habitantes")

        # Información adicional sobre patrones
        st.markdown("---")
        st.markdown("**🔍 Patrones Destacados por Grupos de Edad**")
        
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            st.metric("Mortalidad Violenta 15-24", "56%", "Homicidios")
            
        with col_b:
            st.metric("Diagnósticos Indefinidos", "24%", "25-59 años")
            
        with col_c:
            st.metric("Cardiopatías >60", "24%", "Principal causa")    
    # ---------------------------
    # PESTAÑA 6: Tabla de Mortalidad
    # ---------------------------
    with tab6:
        st.subheader("6. Tabla de Mortalidad - Esperanza de Vida")
        
        col1, col2 = st.columns([1.5, 1])
        
        with col1:
            # Datos completos de esperanza de vida por sexo
            data_esperanza = {
                "Indicador": [
                    "Esperanza de vida al nacer", 
                    "Esperanza de vida a los 15 años",
                    "Esperanza de vida a los 60 años", 
                    "Esperanza de vida a los 85 años"
                ],
                "Hombres": ["75.44 años", "61.61 años", "23.30 años", "7.80 años"],
                "Mujeres": ["82.91 años", "68.79 años", "26.61 años", "8.25 años"],
                "Total": ["79.28 años", "65.31 años", "25.12 años", "8.07 años"]
            }
            df_esperanza = pd.DataFrame(data_esperanza)
            st.dataframe(df_esperanza, use_container_width=True)
            
            # Probabilidades de supervivencia clave
            st.markdown("**📊 Probabilidades de Supervivencia entre Grupos Etarios**")
            
            prob_data = {
                "Transición": [
                    "De 0 a 1-4 años",
                    "De 1-4 a 5-9 años", 
                    "De 75-79 a 80-84 años",
                    "De 80-84 a 85+ años"
                ],
                "Hombres": ["98.79%", "99.91%", "72.06%", "56.64%"],
                "Mujeres": ["99.21%", "99.93%", "80.19%", "59.48%"],
                "Total": ["98.96%", "99.92%", "76.81%", "58.38%"]
            }
            df_prob = pd.DataFrame(prob_data)
            st.dataframe(df_prob, use_container_width=True)
            
            st.markdown("""
            **📈 Análisis de la tabla de mortalidad:**
            - **Ventaja femenina:** Mujeres viven 7.47 años más al nacer
            - **Mortalidad infantil:** Probabilidad perspectiva S₀ < S₁₋₄ refleja alta mortalidad infantil
            - **Edad crítica:** Probabilidad cae drásticamente después de los 75 años
            - **Efecto cohorte:** Diferencia se reduce en edades avanzadas (0.4 años a los 85)
            """)
        
        with col2:
            # Gráfico comparativo de esperanza de vida al nacer
            esperanza_nacer = pd.DataFrame({
                'Sexo': ['Hombres', 'Mujeres', 'Total'],
                'Esperanza_Vida': [75.44, 82.91, 79.28]
            })
            
            chart_esperanza = alt.Chart(esperanza_nacer).mark_bar().encode(
                x=alt.X('Sexo:N', title='Sexo'),
                y=alt.Y('Esperanza_Vida:Q', title='Años de Esperanza de Vida'),
                color=alt.Color('Sexo:N', scale=alt.Scale(
                    domain=['Hombres', 'Mujeres', 'Total'],
                    range=['#1f77b4', '#ff7f0e', '#2ca02c']
                )),
                tooltip=['Sexo', 'Esperanza_Vida']
            ).properties(
                height=250,
                title='Esperanza de Vida al Nacer'
            )
            st.altair_chart(chart_esperanza, use_container_width=True)
            
            # Métricas clave
            st.metric("Diferencia H-M al nacer", "7.47 años", "A favor de mujeres")
            st.metric("Esperanza vida >60 años", "25.12", "Años adicionales")
            st.metric("Reducción 75-79→80-84", "-23.19%", "Probabilidad supervivencia")
            
            # Gráfico de probabilidades de supervivencia
            prob_chart_data = pd.DataFrame({
                'Grupo_Edad': ['0→1-4', '1-4→5-9', '75-79→80-84', '80-84→85+'],
                'Probabilidad': [98.96, 99.92, 76.81, 58.38]
            })
            
            chart_prob = alt.Chart(prob_chart_data).mark_bar().encode(
                x=alt.X('Grupo_Edad:N', title='Transición de Edad'),
                y=alt.Y('Probabilidad:Q', title='Probabilidad (%)'),
                color=alt.Color('Probabilidad:Q', scale=alt.Scale(scheme='blues')),
                tooltip=['Grupo_Edad', 'Probabilidad']
            ).properties(
                height=200,
                title='Probabilidades de Supervivencia'
            )
            st.altair_chart(chart_prob, use_container_width=True)
        
        # Información sobre supuestos metodológicos
        st.markdown("---")
        st.markdown("**🔍 Supuestos Metodológicos de la Tabla de Mortalidad**")
        
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            st.info("""
            **📋 Supuestos:**
            - Cohorte inicial: 100,000 recién nacidos
            - Tasas de mortalidad constantes
            - Periodo de observación: 2023
            - Desaparición solo por mortalidad
            - Homogeneidad de condiciones
            """)
        
        with col_b:
            st.success("""
            **✅ Hallazgos Clave:**
            - Efecto mortalidad infantil visible
            - Ventaja femenina en todas las edades
            - Caída drástica después de los 75 años
            - Sincronía con estructura poblacional
            """)
        
        with col_c:
            st.warning("""
            **📝 Notas Técnicas:**
            - Probabilidad perspectiva: Sₓ
            - Esperanza de vida: eₓ
            - Tasas específicas: mₓ
            - Base: Proyecciones DANE 2023
            """)
    
    # ---------------------------
    # PESTAÑA 7: Comparación Nacional
    # ---------------------------
    with tab7:
        st.subheader("7. Comparación con el País")
        
        col1, col2 = st.columns([1.5, 1])
        
        with col1:
            st.markdown("**📊 Comparativa de Indicadores Demográficos**")
            
            comparativa_nacional = {
                "Indicador": [
                    "Esperanza de vida - Hombres", 
                    "Esperanza de vida - Mujeres",
                    "Esperanza de vida - Total",
                    "Esperanza de vida >80 años",
                    "Tasa Bruta de Mortalidad",
                    "Mortalidad Infantil"
                ],
                "Valle del Cauca": ["75.4 años", "83.0 años", "79.3 años", "~11.1 años", "6.27", "10.08"],
                "Colombia (ONU)": ["74.8 años", "82.5 años", "78.7 años", "~10.5 años", "~6.5", "~11.5"],
                "Diferencia": ["+0.6 años", "+0.5 años", "+0.6 años", "+0.6 años", "-0.23", "-1.42"]
            }
            df_nacional = pd.DataFrame(comparativa_nacional)
            st.dataframe(df_nacional, use_container_width=True)
            
            st.markdown("""
            **📈 Análisis Comparativo:**
            - **Ventaja en esperanza de vida:** Superior en todos los grupos etarios
            - **Mayor diferencia en adultos mayores:** +0.6 años después de los 80
            - **Mortalidad infantil:** Significativamente mejor (-1.42)
            - **Envejecimiento poblacional:** Más avanzado vs país
            """)
        
        with col2:
            st.markdown("**🎯 Posición Relativa vs Colombia**")
            
            st.metric("Esperanza Vida Total", "+0.6 años", "Superior al promedio nacional")
            st.metric("Mortalidad Infantil", "-1.42", "12% mejor que nacional")
            st.metric("Esperanza >80 años", "+0.6 años", "Mayor envejecimiento saludable")
            st.metric("TBM", "-0.23", "Ligeramente mejor")
            
            # Gráfico de diferencias
            diff_data = pd.DataFrame({
                'Indicador': ['Esp. Vida H', 'Esp. Vida M', 'Esp. Vida T', 'Mortal. Infantil'],
                'Diferencia': [0.6, 0.5, 0.6, -1.42]
            })
            
            chart_diff = alt.Chart(diff_data).mark_bar().encode(
                x=alt.X('Indicador:N', title='Indicador'),
                y=alt.Y('Diferencia:Q', title='Diferencia (Valle - Colombia)'),
                color=alt.condition(
                    alt.datum.Diferencia > 0,
                    alt.value('#2ca02c'),  # Verde para positivo
                    alt.value('#d62728')   # Rojo para negativo
                ),
                tooltip=['Indicador', 'Diferencia']
            ).properties(
                height=250,
                title='Diferencias vs Promedio Nacional'
            )
            st.altair_chart(chart_diff, use_container_width=True)
        
        # Análisis de correspondencia y diferencias
        st.markdown("---")
        st.markdown("**🔍 Análisis de Correspondencia con el País**")
        
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            st.success("""
            **✅ Semejanzas:**
            - Patrones de mortalidad similares
            - Estructura por causas comparable
            - Tendencia de ventaja femenina
            - Curva de mortalidad en forma de U
            """)
        
        with col_b:
            st.warning("""
            **📊 Diferencias:**
            - Mayor esperanza de vida
            - Menor mortalidad infantil
            - Población más envejecida
            - Mejores indicadores generales
            """)
        
        with col_c:
            st.info("""
            **🎯 Contexto:**
            - Diferencias no sustanciales
            - Correspondencia en mediciones
            - Volúmenes poblacionales diferentes
            - Mismos patrones demográficos
            """)
        
        st.info("""
        **📌 Conclusión General:** 
        *"El fenómeno de la mortalidad en el departamento no es ajeno al país, existe, pues, 
        una correspondencia en muchas de sus mediciones entre país y departamento, dejando 
        de lado las mediciones de volúmenes poblacionales que naturalmente se alejan."*
        
        - El Valle del Cauca supera los promedios nacionales en esperanza de vida
        - Presenta menor mortalidad infantil que el promedio del país
        - Las diferencias, aunque favorables, no son sustanciales
        - Existe correspondencia en los patrones de mortalidad con el nivel nacional
        """)

    # Footer informativo
    st.markdown("---")
    st.caption("Fuentes: DANE - Proyecciones Poblacionales y Estadísticas Vitales 2023 | ONU - Estimaciones Colombia 2023 | Elaboración propia")
# -----------------------------------------------------------
# SECCIÓN: Fecundidad (2023) - VALLE DEL CAUCA
# -----------------------------------------------------------
elif section == "👶 Fecundidad (2023)":
    st.header("👶 Análisis de Fecundidad - Valle del Cauca 2023")
    
    # ---------------------------
    # 1️⃣ Indicadores Generales
    # ---------------------------
    st.subheader("📊 Indicadores Generales de Fecundidad")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Tasa Bruta de Natalidad", "7.81", help="Por 1000 habitantes")
        st.metric("Total Nacimientos", "36,514")
    
    with col2:
        st.metric("Tasa General de Fecundidad (TGF)", "29.61", help="Por 1000 mujeres en edad fértil")
        st.metric("Población Media 2023", "4,673,395")
    
    with col3:
        st.metric("Índice Sintético de Fecundidad (ISF)", "0.99", help="Hijos por mujer")
        st.metric("Edad Media Materna (EMM)", "29.96 años")
    
    with col4:
        st.metric("Tasa Bruta de Reproductividad (TBR)", "0.49")
        st.metric("Tasa Neta de Reproducción (TNR)", "0.47")
    
    st.markdown("---")
    
    # ---------------------------
    # 2️⃣ Comparativa Nacional vs Valle
    # ---------------------------
    st.subheader("📈 Comparativa con Promedios Nacionales")
    
    comparativa_data = {
        "Indicador": ["Tasa Bruta de Natalidad", "Índice Sintético de Fecundidad", 
                     "Tasa Neta de Reproducción", "Edad Media Materna"],
        "Valle del Cauca": ["7.81‰", "0.99 hijos/mujer", "0.47", "29.96 años"],
        "Colombia (ONU)": ["13.5‰", "1.65 hijos/mujer", "0.79", "26.6 años"],
        "Diferencia": ["-5.69‰", "-0.66 hijos", "-0.32", "+3.36 años"]
    }
    df_comparativa = pd.DataFrame(comparativa_data)
    
    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        st.dataframe(df_comparativa, use_container_width=True)
    
    with col2:
        st.warning("""
        **🔍 Hallazgos Clave:**
        - Natalidad 42% menor que el promedio nacional
        - Fecundidad por debajo del nivel de reemplazo
        - Maternidad más tardía (+3.4 años)
        - Menor capacidad de reemplazo generacional
        """)
    
    st.markdown("---")
    
    # ---------------------------
    # 3️⃣ Nacimientos por Edad de la Madre
    # ---------------------------
    st.subheader("👩‍👧 Nacimientos Ocurridos según Edad de la Madre - 2023")
    
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        data_nacimientos = {
            "Grupos de edad": ["15-19", "20-24", "25-29", "30-34", "35-39", "40-44", "45-49", "15-49"],
            "Total": [4369, 9843, 9961, 7381, 3728, 951, 53, 36286]
        }
        df_nacimientos = pd.DataFrame(data_nacimientos)
        st.dataframe(df_nacimientos, use_container_width=True)
        
        # Frecuencia relativa
        st.markdown("**📋 Distribución Porcentual:**")
        st.markdown("- **20-29 años:** 53% del total")
        st.markdown("- **30-34 años:** 20% del total") 
        st.markdown("- **15-19 años:** 12% del total")
    
    with col2:
        # Gráfico de barras de nacimientos
        df_nac_chart = df_nacimientos[df_nacimientos["Grupos de edad"] != "15-49"]
        
        chart_nac = alt.Chart(df_nac_chart).mark_bar(color="#eb0eff").encode(
            x=alt.X("Grupos de edad:N", title="Edad de la Madre", sort=None),
            y=alt.Y("Total:Q", title="Número de Nacimientos"),
            tooltip=["Grupos de edad", "Total"]
        ).properties(
            title="Distribución de Nacimientos por Edad de la Madre",
            height=300
        )
        st.altair_chart(chart_nac, use_container_width=True)
        
        st.info("""
        **🎯 Patrón de Fecundidad:**
        - **Cúspide temprana:** 20-29 años (53% concentración)
        - **Importancia relevante:** 30-34 años (20%)
        - **Fecundidad adolescente:** 12% (15-19 años)
        """)
    
    st.markdown("---")
    
    # ---------------------------
    # 4️⃣ Tasas Específicas de Fecundidad (TEF)
    # ---------------------------
    st.subheader("📈 Tasas Específicas de Fecundidad por Edad - 2023")
    
    data_tef = {
        "Grupos de edad": ["15-19", "20-24", "25-29", "30-34", "35-39", "40-44", "45-49"],
        "TEF": [25.01, 54.00, 51.60, 40.15, 21.90, 5.66, 0.35],
        "Frecuencia Relativa": ["13%", "27%", "26%", "20%", "11%", "3%", "0%"]
    }
    df_tef = pd.DataFrame(data_tef)
    
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.dataframe(df_tef, use_container_width=True)
    
    with col2:
        # Gráfico TEF
        chart_tef = alt.Chart(df_tef).mark_line(point=True, color="#009e73", size=3).encode(
            x=alt.X("Grupos de edad:N", title="Grupo de Edad", sort=None),
            y=alt.Y("TEF:Q", title="TEF (por 1000 mujeres)", scale=alt.Scale(domain=[0, 60])),
            tooltip=["Grupos de edad", alt.Tooltip("TEF:Q", format=".2f")]
        ).properties(
            title="Tasa Específica de Fecundidad (TEF) por Edad",
            height=400
        )
        st.altair_chart(chart_tef, use_container_width=True)
    
    st.markdown("---")
    
    # ---------------------------
    # 5️⃣ Población de Mujeres y Tasas de Reproducción
    # ---------------------------
    st.subheader("👩 Población y Reproducción - 2023")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Población Media de Mujeres en Edad Fértil**")
        data_pob_mujeres = {
            "Grupos de edad": ["15-19", "20-24", "25-29", "30-34", "35-39", "40-44", "45-49", "15-49"],
            "Población": [174705, 182282, 193056, 183836, 170249, 168153, 153293, 1225574]
        }
        df_pob_mujeres = pd.DataFrame(data_pob_mujeres)
        st.dataframe(df_pob_mujeres, use_container_width=True, height=300)
    
    with col2:
        st.markdown("**Tasas de Reproducción por Edad**")
        data_reproduccion = {
            "Grupos de edad": ["15-19", "20-24", "25-29", "30-34", "35-39", "40-44", "45-49", "15-49 TNR"],
            "TEFm": [12.09, 26.60, 25.42, 19.34, 10.81, 2.75, 0.18, "-"],
            "TNR": ["-", "-", "-", "-", "-", "-", "-", "0.47"]
        }
        df_reproduccion = pd.DataFrame(data_reproduccion)
        st.dataframe(df_reproduccion, use_container_width=True, height=300)
        
        st.metric("Nacimientos Niñas Totales", "17,865")
    
    st.markdown("---")
    
    # ---------------------------
    # 6️⃣ Análisis de Reemplazo Generacional
    # ---------------------------
    st.subheader("🔄 Análisis de Reemplazo Generacional")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Tasa Bruta Reproductividad", "0.49", 
                 help="Niñas por mujer sin considerar mortalidad")
        
    with col2:
        st.metric("Tasa Neta Reproducción", "0.47", 
                 help="Niñas por mujer considerando mortalidad")
        
    with col3:
        st.metric("Nivel de Reemplazo", "47%", 
                 "Del nivel necesario para mantenimiento")
    
    st.error("""
    **⚠️ Situación Demográfica:**
    - **Fecundidad por debajo del reemplazo:** 0.99 vs 2.1 necesario
    - **Baja capacidad de reemplazo:** TNR = 0.47
    - **Posible disminución poblacional:** Sin considerar migración
    - **Envejecimiento acelerado:** Estructura poblacional cambiante
    """)
    
    st.success("""
    **✅ Conclusión General:**
    *"El departamento del Valle del Cauca presenta menores niveles de fecundidad respecto al país, 
    con tasas de reemplazo también bajas. Mostrando con ella, posibles disminuciones del volumen 
    poblacional mayores en el departamento que en el país sin analizar el efecto de la mortalidad 
    y la migración."*
    
    - Fecundidad inferior al promedio nacional en todos los indicadores
    - Maternidad más tardía que el promedio colombiano
    - Capacidad de reemplazo generacional insuficiente
    - Concentración de fecundidad en edades 20-34 años
    """)


# -----------------------------------------------------------
# SECCIONES RESTANTES (placeholder)
# -----------------------------------------------------------
elif section == "🚶‍♂️ Migración (2018)":
    st.header("🚶‍♂️ Análisis de Migración - Área Metropolitana de Cali (2013-2018)")
    
    # ---------------------------
    # DEFINICIÓN DEL ÁREA METROPOLITANA
    # ---------------------------
    st.markdown("""
    ### 📍 Definición del Área Metropolitana de Cali
    El área metropolitana definido es:
    - **Cali** (núcleo central)
    - **Yumbo** (municipio contiguo industrial)
    - **Jamundí** (municipio contiguo de expansión)
    - **Palmira** (municipio contiguo estratégico)
    """)
    
    
    # ---------------------------
    # DATOS ACTUALIZADOS CON LA NUEVA TABLA
    # ---------------------------
    st.subheader("📊 Indicadores de Migración - Área Metropolitana de Cali")
    
    # Definir municipios del área metropolitana
    municipios_metro = ["Cali", "Yumbo", "Jamundí", "Palmira"]
    
    data_migracion = {
        "Municipio": [
            "Total", "Cali", "Alcalá", "Andalucía", "Ansermanuevo", "Argelia", "Bolívar", 
            "Buenaventura", "Guadalajara de BUGA", "Bugalagrande", "Caicedonia", "Calima", 
            "Candelaria", "Cartago", "Dagua", "El Águila", "El Cairo", "El Cerrito", 
            "El Dovio", "Florida", "Ginebra", "Guacarí", "Jamundí", "La Cumbre", 
            "La Unión", "La Victoria", "Obando", "Palmira", "Pradera", "Restrepo", 
            "Riofrío", "Roldanillo", "San Pedro", "Sevilla", "Toro", "Trujillo", 
            "Tuluá", "Ulloa", "Versalles", "Vijes", "Yotoco", "Yumbo", "Zarzal"
        ],
        "Poblacion_2018": [
            3323114, 1616798, 9287, 15975, 14385, 4499, 13072, 231870, 101853, 19468, 
            22265, 15157, 71258, 102053, 34090, 6263, 5499, 47840, 7827, 49906, 17722, 
            27104, 93251, 10385, 24738, 9796, 9883, 262446, 39085, 11526, 12247, 27161, 
            13093, 32651, 10885, 14314, 165754, 3942, 5920, 9074, 12789, 85148, 34835
        ],
        "Poblacion_2013": [
            3323114, 1594851, 9483, 16296, 13848, 4401, 12604, 225194, 102160, 19695, 
            14048, 75055, 102842, 35032, 6303, 5381, 48710, 7477, 49357, 17420, 27124, 
            109418, 11307, 25595, 9815, 9708, 267555, 38984, 11306, 12491, 27915, 13751, 
            32130, 10772, 14588, 165063, 3985, 5609, 9701, 13641, 85365, 34806, 34548
        ],
        "Inmigrantes": [
            115656, 23205, 707, 1183, 696, 344, 352, 2097, 3979, 1582, 1042, 1425, 
            5456, 3839, 2512, 550, 391, 2289, 506, 955, 584, 1250, 18941, 1529, 2064, 
            681, 541, 11642, 1345, 877, 1273, 2141, 1317, 1467, 765, 1393, 6965, 215, 
            360, 980, 1563, 3032, 1621
        ],
        "Emigrantes": [
            115656, 45152, 511, 862, 1233, 442, 820, 8773, 3672, 1355, 979, 2534, 
            1659, 3050, 1570, 510, 509, 1419, 856, 1504, 886, 1230, 2774, 607, 1207, 
            662, 716, 6533, 1446, 1097, 1029, 1387, 659, 1988, 878, 1119, 7656, 172, 
            671, 353, 711, 2815, 1650
        ],
        "Migracion_Neta": [
            0, -21947, 196, 321, -537, -98, -468, -6676, 307, 227, 63, -1109, 3797, 
            789, 942, 40, -118, 870, -350, -549, -302, 20, 16167, 922, 857, 19, -175, 
            5109, -101, -220, 244, 754, 658, -521, -113, 274, -691, 43, -311, 627, 852, 
            217, -29
        ],
        "Tasa_Inmigracion": [
            6.96, 2.89, 15.07, 14.66, 9.86, 15.46, 5.48, 1.84, 7.80, 16.16, 9.35, 
            19.52, 14.92, 7.49, 14.54, 17.51, 14.38, 9.48, 13.23, 3.85, 6.65, 9.22, 
            37.38, 28.19, 16.40, 13.89, 11.05, 8.79, 6.89, 15.36, 20.58, 15.55, 19.62, 
            9.06, 14.13, 19.28, 8.42, 10.85, 12.49, 20.88, 23.65, 7.11, 9.31
        ],
        "Tasa_Emigracion": [
            6.96, 5.62, 10.89, 10.68, 17.47, 19.87, 12.77, 7.68, 7.20, 13.84, 8.78, 
            34.71, 4.54, 5.95, 9.09, 16.23, 18.71, 5.88, 22.37, 6.06, 10.08, 9.07, 
            5.47, 11.19, 9.59, 13.50, 14.62, 4.93, 7.41, 19.22, 16.64, 10.07, 9.82, 
            12.28, 16.22, 15.49, 9.26, 8.68, 23.28, 7.52, 10.76, 6.60, 9.48
        ],
        "Tasa_Migracion": [
            0.00, -2.73, 4.18, 3.98, -7.61, -4.40, -7.29, -5.84, 0.60, 2.32, 0.57, 
            -15.19, 10.38, 1.54, 5.45, 1.27, -4.34, 3.60, -9.15, -2.21, -3.44, 0.15, 
            31.91, 17.00, 6.81, 0.39, -3.57, 3.86, -0.52, -3.85, 3.95, 5.48, 9.80, 
            -3.22, -2.09, 3.79, -0.84, 2.17, -10.79, 13.36, 12.89, 0.51, -0.17
        ]
    }
    
    df_migracion = pd.DataFrame(data_migracion)
    
    # Filtrar datos del área metropolitana
    df_metro = df_migracion[df_migracion["Municipio"].isin(municipios_metro)].copy()
    
    # Calcular totales del área metropolitana
    total_metro = {
        "Poblacion_2018": df_metro["Poblacion_2018"].sum(),
        "Poblacion_2013": df_metro["Poblacion_2013"].sum(),
        "Inmigrantes": df_metro["Inmigrantes"].sum(),
        "Emigrantes": df_metro["Emigrantes"].sum(),
        "Migracion_Neta": df_metro["Migracion_Neta"].sum()
    }
    
    total_metro["Poblacion_Media"] = (total_metro["Poblacion_2018"] + total_metro["Poblacion_2013"]) / 2
    total_metro["Tasa_Inmigracion"] = (total_metro["Inmigrantes"] / total_metro["Poblacion_Media"]) * 1000
    total_metro["Tasa_Emigracion"] = (total_metro["Emigrantes"] / total_metro["Poblacion_Media"]) * 1000
    total_metro["Tasa_Migracion"] = total_metro["Tasa_Inmigracion"] - total_metro["Tasa_Emigracion"]
    
    # ---------------------------
    # INDICADORES DEL ÁREA METROPOLITANA
    # ---------------------------
    st.subheader("🎯 Indicadores Clave del Área Metropolitana")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Población Total 2018", f"{total_metro['Poblacion_2018']:,.0f}")
        st.metric("Población Media", f"{total_metro['Poblacion_Media']:,.0f}")
    
    with col2:
        st.metric("Migración Neta", f"{total_metro['Migracion_Neta']:+,.0f}")
        st.metric("Tasa Migración Neta", f"{total_metro['Tasa_Migracion']:+.2f}")
    
    with col3:
        st.metric("Total Inmigrantes", f"{total_metro['Inmigrantes']:,.0f}")
        st.metric("Total Emigrantes", f"{total_metro['Emigrantes']:,.0f}")
    
    with col4:
        st.metric("Tasa Inmigración", f"{total_metro['Tasa_Inmigracion']:.2f}")
        st.metric("Tasa Emigración", f"{total_metro['Tasa_Emigracion']:.2f}")
    
    # ---------------------------
    # COMPARATIVA MUNICIPIOS METROPOLITANOS
    # ---------------------------
    st.subheader("🏙️ Comparativa entre Municipios del Área Metropolitana")
    
    # Mostrar tabla comparativa
    display_metro = df_metro.copy()
    # Formatear números para mejor visualización
    numeric_cols = ['Poblacion_2018', 'Poblacion_2013', 'Inmigrantes', 'Emigrantes', 'Migracion_Neta']
    for col in numeric_cols:
        display_metro[col] = display_metro[col].apply(lambda x: f"{x:,.0f}")
    
    # Formatear tasas con 2 decimales
    tasa_cols = ['Tasa_Inmigracion', 'Tasa_Emigracion', 'Tasa_Migracion']
    for col in tasa_cols:
        display_metro[col] = display_metro[col].apply(lambda x: f"{x:.2f}")
    
    st.dataframe(display_metro.set_index("Municipio"), use_container_width=True)
    
    # ---------------------------
    # GRÁFICOS COMPARATIVOS
    # ---------------------------
    col1, col2 = st.columns(2)
    
    with col1:
        # Gráfico de migración neta comparativa
        chart_comparativo = alt.Chart(df_metro).mark_bar().encode(
            x=alt.X('Migracion_Neta:Q', title='Migración Neta (personas)'),
            y=alt.Y('Municipio:N', sort='-x', title='Municipio'),
            color=alt.condition(
                alt.datum.Migracion_Neta > 0,
                alt.value("#2E8B57"),  # Verde
                alt.value("#CD5C5C")   # Rojo
            ),
            tooltip=['Municipio', 'Migracion_Neta', 'Tasa_Migracion']
        ).properties(
            title='Migración Neta - Área Metropolitana',
            height=300
        )
        st.altair_chart(chart_comparativo, use_container_width=True)
    
    with col2:
        # Gráfico de tasas de migración
        chart_tasas = alt.Chart(df_metro).mark_bar().encode(
            x=alt.X('Tasa_Migracion:Q', title='Tasa de Migración Neta'),
            y=alt.Y('Municipio:N', sort='-x', title='Municipio'),
            color=alt.condition(
                alt.datum.Tasa_Migracion > 0,
                alt.value("#1E90FF"),  # Azul
                alt.value("#FF6347")   # Rojo anaranjado
            ),
            tooltip=['Municipio', 'Tasa_Migracion']
        ).properties(
            title='Tasa de Migración Neta - Área Metropolitana',
            height=300
        )
        st.altair_chart(chart_tasas, use_container_width=True)
    
    # ---------------------------
    # ANÁLISIS DE FLUJOS MIGRATORIOS
    # ---------------------------
    st.subheader("📈 Análisis de Flujos Migratorios Metropolitanos")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📊 Flujos de Entrada y Salida")
        
        # Gráfico de tasas de inmigración vs emigración
        df_tasas_comparadas = df_metro.melt(
            id_vars=['Municipio'], 
            value_vars=['Tasa_Inmigracion', 'Tasa_Emigracion'],
            var_name='Tipo_Tasa', 
            value_name='Valor_Tasa'
        )
        
        df_tasas_comparadas['Tipo'] = df_tasas_comparadas['Tipo_Tasa'].map({
            'Tasa_Inmigracion': 'Inmigración',
            'Tasa_Emigracion': 'Emigración'
        })
        
        chart_tasas_comparadas = alt.Chart(df_tasas_comparadas).mark_bar().encode(
            x=alt.X('Valor_Tasa:Q', title='Tasa'),
            y=alt.Y('Municipio:N', title='Municipio'),
            color=alt.Color('Tipo:N', 
                          scale=alt.Scale(domain=['Inmigración', 'Emigración'], 
                                        range=['#2E8B57', '#CD5C5C'])),
            column=alt.Column('Tipo:N', header=alt.Header(title=None))
        ).properties(
            width=200,
            height=300,
            title='Tasas de Inmigración vs Emigración'
        )
        st.altair_chart(chart_tasas_comparadas)
    
    with col2:
        st.markdown("### 🎯 Balance Migratorio Municipal")
        
        # Resumen de balances
        st.metric("Saldo Migratorio Metropolitano", f"{total_metro['Migracion_Neta']:+,.0f} personas")
        st.metric("Tasa Migratoria Metropolitana", f"{total_metro['Tasa_Migracion']:+.2f}")
        
        st.markdown("**Distribución municipal:**")
        for _, municipio in df_metro.iterrows():
            icono = "🟢" if municipio['Migracion_Neta'] > 0 else "🔴" if municipio['Migracion_Neta'] < 0 else "🟡"
            st.write(f"{icono} **{municipio['Municipio']}:** {municipio['Migracion_Neta']:+,.0f} personas ({municipio['Tasa_Migracion']:+.2f})")
    
    # ---------------------------
    # ANÁLISIS ESPECIAL: JAMUNDÍ COMO CASO DESTACADO
    # ---------------------------
    st.markdown("---")
    st.subheader("🌟 Caso de Estudio: Jamundí")
    
    jamundi_data = df_metro[df_metro["Municipio"] == "Jamundí"].iloc[0]
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Tasa Migración Neta", f"{jamundi_data['Tasa_Migracion']:.2f}")
    
    with col2:
        st.metric("Tasa Inmigración", f"{jamundi_data['Tasa_Inmigracion']:.2f}")
    
    with col3:
        st.metric("Tasa Emigración", f"{jamundi_data['Tasa_Emigracion']:.2f}")
    
    st.info("""
    **💡 Análisis del fenómeno en Jamundí:**
    - **Alta tasa de inmigración (37.38):** Una de las más altas de la región
    - **Baja tasa de emigración (5.47):** Excelente retención de población
    - **Tasa neta excepcional (31.91):** Fuerte atracción migratoria
    - **Patrón de expansión metropolitana:** Receptor natural de la expansión de Cali
    - **Movimientos netos positivos:** 16,167 personas ganadas por migración
    """)
    # ---------------------------
    # MOSTRAR MAPA GUARDADO
    # ---------------------------
    st.subheader("🗺️ Mapa de Tasas de Migración - Valle del Cauca")
    
    # Mostrar la imagen del mapa generado en R
    try:
        st.image("mapa_tasa_migracion_valle_cauca.png", 
                caption="Mapa de Tasas de Migración Neta - Departamento del Valle del Cauca (2013-2018)",
                use_container_width=True)
        
        st.info("""
        **🔍 Interpretación del Mapa:**
        - **🟢 Verde:** Municipios receptores (ganan población por migración)
        - **🔴 Rojo:** Municipios expulsores (pierden población por migración)  
        - **⬛ Borde negro:** Municipios del Área Metropolitana de Cali
        - **📊 Escala:** Tasas por mil habitantes (2013-2018)
        """)
        
    except FileNotFoundError:
        st.warning("⚠️ El archivo del mapa no se encuentra en la carpeta.")
        st.info("""
        **Para generar el mapa:**
        1. Ejecuta el código R proporcionado
        2. Guarda la imagen como 'mapa_tasa_migracion_valle_cauca.png'
        3. Asegúrate de que esté en la misma carpeta que este script Python
        """)
    
    # ---------------------------
    # CONCLUSIONES ESTRATÉGICAS
    # ---------------------------
    st.markdown("---")
    st.subheader("💡 Conclusiones Estratégicas para el Área Metropolitana")
    
    conclusion_col1, conclusion_col2 = st.columns(2)
    
    with conclusion_col1:
        st.markdown("""
        **✅ Fortalezas del Sistema Metropolitano:**
        
        - **Alta capacidad de atracción:** Jamundí lidera con 31.91
        - **Balance positivo general:** Tasa neta metropolitana positiva
        - **Eficiencia en movimientos:** Saldo neto positivo de 14,546 personas
        - **Diversificación espacial:** Crecimiento distribuido en múltiples polos
        - **Retención de población:** Bajas tasas de emigración en municipios receptores
        """)
    
    with conclusion_col2:
        st.markdown("""
        **📋 Recomendaciones de Política:**
        
        - **Fortalecer conectividad** entre municipios metropolitanos
        - **Planificar expansión urbana** coordinada
        - **Invertir en servicios** en municipios receptores (Jamundí, Palmira)
        - **Gestionar presión demográfica** en áreas de alta atracción
        - **Monitorear flujos migratorios** para planificación de servicios
        """)
    
    st.info("""
    **🎯 Resumen Ejecutivo del Área Metropolitana (2013-2018):**
    
    - **Población total 2018:** 2,009,543 habitantes
    - **Saldo migratorio neto:** 14,546 personas
    - **Tasa de migración neta:** 8.36 (vs promedio negativo no metropolitano)
    - **Jamundí destaca** con tasa migratoria de 31.91
    - **Cali muestra** patrón de expulsión neta (-2.73) dentro del sistema
    - **Sistema equilibrado:** 3 municipios receptores vs 1 expulsor
    """)

# Footer informativo
st.markdown("---")
st.caption("Fuente: Censo DANE 2013-2018 | Definición Área Metropolitana: CEPAL | Elaboración propia")
