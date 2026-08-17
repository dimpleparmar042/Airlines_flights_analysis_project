import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
#
st.set_page_config(page_title='Airlines Flights Dashboard',page_icon='✈️',layout='wide')
df=pd.read_csv('airlines_flights_data.csv')
with st.sidebar:
    opt=option_menu(menu_title='Airlines Menu',options=['Home','Dataset Overview','Pre-Processing','Visualization','About'],icons=['house','table','gear','bar-chart','info-circle'],default_index=0

    )

st.markdown(
    """
    <style>
    /* Main app background */
    .stApp {
        background-color: #0c192c;
        color: #ffffff;
    }

    /* Sidebar background */
    [data-testid="stSidebar"] {
        background-color: #162d49;
    }

    /* Change text color in sidebar */
    [data-testid="stSidebar"] * {
        color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
if opt == "Home":

    # Column names
    airline_col = "airline" if "airline" in df.columns else "Airline"
    source_col = "source_city" if "source_city" in df.columns else "Source"
    dest_col = "destination_city" if "destination_city" in df.columns else "Destination"

    # Home page CSS
    st.markdown(
        """
        <style>

        /* Title */
        .home-title {
    background: linear-gradient(135deg, #00f2fe 0%, #4facfe 50%, #00c6ff 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 2.8rem !important;
    font-weight: 800 !important;
    margin-bottom: 0px;
    text-shadow: 0px 10px 20px rgba(0, 242, 254, 0.2);
}
        }

        /* Subtitle */
        .home-caption {
            color: #a0aec0;
            font-size: 1.1rem;
            margin-bottom: 20px;
        }

        /* Cards */
        .custom-card {
            background: rgba(22, 45, 73, 0.65);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 16px;
            padding: 22px;
            margin-bottom: 15px;
            transition: 0.4s;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.37);
        }

        /* Card hover */
        .custom-card:hover {
            transform: translateY(-8px) scale(1.02);
            border-color: rgba(0, 242, 254, 0.5);
            box-shadow: 0 15px 30px rgba(0, 242, 254, 0.25);
        }

        /* Card left borders */
        .card-objective {
            border-left: 5px solid #00f2fe;
        }

        .card-dataset {
            border-left: 5px solid #00e676;
        }

        /* KPI cards */
        [data-testid="stMetric"] {
            background: rgba(22, 45, 73, 0.5);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 14px;
            padding: 15px;
            transition: 0.3s;
        }

        [data-testid="stMetric"]:hover {
            transform: translateY(-5px);
            border-color: #ffd700;
            box-shadow: 0 10px 20px rgba(255, 215, 0, 0.2);
        }

        [data-testid="stMetricLabel"] {
            color: #e2e8f0;
            font-weight: 600;
        }

        [data-testid="stMetricValue"] {
            color: #00f2fe;
            font-weight: 800;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    # Title
    st.markdown(
        "<h1 class='home-title'>✈️ Airlines Flight Data Analysis Dashboard</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p class='home-caption'>A comprehensive analytics platform for evaluating flight pricing trends, route patterns, and airline performance.</p>",
        unsafe_allow_html=True
    )

    st.divider()

    # Project Objective and Dataset
    col_info1, col_info2 = st.columns(2)

    with col_info1:
        st.markdown(
            """
            <div class="custom-card card-objective">
                <h3 style="color:#00f2fe;">📌 Project Objective</h3>
                <p style="color:#e2e8f0; font-size:0.98rem; line-height:1.6;">
                The main objective of this project is to analyze airline flight data,
                identify ticket price trends across carriers, compare operational
                performance, and uncover insights into popular travel routes.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_info2:
        st.markdown(
            """
            <div class="custom-card card-dataset">
                <h3 style="color:#00e676;">📊 About the Dataset</h3>
                <p style="color:#e2e8f0; font-size:0.98rem; line-height:1.6;">
                This dataset contains structured flight information, including carrier
                names, departure and arrival cities, flight durations, stop details,
                and ticket pricing across major routes.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("<br>", unsafe_allow_html=True)

    # Quick Dataset Summary
    st.subheader("📈 Quick Dataset Summary")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("TOTAL FLIGHTS", f"{len(df):,}")

    col2.metric(
        "TOTAL AIRLINES",
        df[airline_col].nunique() if airline_col in df.columns else "N/A"
    )

    col3.metric(
        "SOURCE CITIES",
        df[source_col].nunique() if source_col in df.columns else "N/A"
    )

    col4.metric(
        "DESTINATION CITIES",
        df[dest_col].nunique() if dest_col in df.columns else "N/A"
    )

    st.divider()

    # Dashboard Features
    st.subheader("🚀 Dashboard Key Features")

    col_feat1, col_feat2 = st.columns(2)

    with col_feat1:
        st.markdown(
        """
        <div class="custom-card">
            <ul style="color:#e2e8f0; list-style-type: none; padding-left: 0; margin-bottom:0;">
                <li style="margin-bottom: 12px;">💰 <strong style="color:#ffd700;">Price Analysis:</strong> Explore pricing behavior across economy and business classes.</li>
                <li>🛣️ <strong style="color:#00f2fe;">Route Insights:</strong> Compare flight durations, stop counts, and city pairings.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )
    with col_feat2:
        st.markdown(
        """
            <div class="custom-card">
            <p style="color:#e2e8f0;">
            📊 <strong style="color:#00e676;">Interactive Charts:</strong>
            Dynamic visual filtering by airline and origin city.
            </p>

            <p style="color:#e2e8f0;">
            💡 <strong style="color:#ff7043;">Business Analytics:</strong>
            Data-backed conclusions to evaluate airline competitiveness.
            </p>
            </div>
                    """,
                    unsafe_allow_html=True,
    )
elif opt == "Dataset Overview":

    # Column names
    airline_col = "airline" if "airline" in df.columns else "Airline"
    source_col = "source_city" if "source_city" in df.columns else "Source_City"

    # ---------------- CSS ----------------
    st.markdown("""
    <style>

    /* Main Heading */
    .overview-title {
        background: linear-gradient(135deg, #00f2fe, #4facfe, #00c6ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;

        font-size: 2.5rem;
        font-weight: 800;

        /* Light Spark Effect */
        text-shadow:
            0 0 6px rgba(0, 242, 254, 0.35),
            0 0 14px rgba(0, 242, 254, 0.20);
    }

    /* Subtitle */
    .overview-subtitle {
        color: #a0aec0;
        font-size: 1rem;
        text-shadow: 0 0 6px rgba(160, 174, 192, 0.15);
    }

    /* Summary Cards */
    .summary-card {
        background: rgba(22, 45, 73, 0.65);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 14px;
        padding: 18px;
        text-align: center;
        margin-bottom: 15px;

        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.30);

        transition: 0.3s;
    }

    .summary-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0, 242, 254, 0.20);
    }

    .card-title {
        color: #a0aec0;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1px;
    }

    .card-value {
        font-size: 25px;
        font-weight: 800;
        margin-top: 5px;
    }

    </style>
    """, unsafe_allow_html=True)


    # ---------------- HEADER ----------------

    st.markdown(
        "<h1 class='overview-title'>📋 Dataset Overview & Interactive Explorer</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p class='overview-subtitle'>Inspect raw records, statistics, column types, and filtered previews.</p>",
        unsafe_allow_html=True
    )

    st.divider()


    # ---------------- SUMMARY CARDS ----------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            f"""
            <div class="summary-card"
                 style="border-top:4px solid #00f2fe;">
                <div class="card-title">TOTAL RECORDS</div>
                <div class="card-value" style="color:#00f2fe;">
                    {len(df):,}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="summary-card"
                 style="border-top:4px solid #00e676;">
                <div class="card-title">TOTAL COLUMNS</div>
                <div class="card-value" style="color:#00e676;">
                    {df.shape[1]}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <div class="summary-card"
                 style="border-top:4px solid #ffd700;">
                <div class="card-title">MISSING VALUES</div>
                <div class="card-value" style="color:#ffd700;">
                    {df.isnull().sum().sum()}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            f"""
            <div class="summary-card"
                 style="border-top:4px solid #ff5252;">
                <div class="card-title">DUPLICATE ROWS</div>
                <div class="card-value" style="color:#ff5252;">
                    {df.duplicated().sum()}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    st.markdown("<br>", unsafe_allow_html=True)


    # ---------------- DATA INSPECTION ----------------

    st.subheader("📑 Data Inspection Tabs")

    tab1, tab2, tab3, tab4 = st.tabs([
        "🔍 First 10 Rows",
        "🔚 Last 10 Rows",
        "📐 Statistical Summary",
        "⚙️ Schema & Data Types"
    ])


    # First 10 Rows
    with tab1:
        st.dataframe(
            df.head(10),
            use_container_width=True
        )


    # Last 10 Rows
    with tab2:
        st.dataframe(
            df.tail(10),
            use_container_width=True
        )


    # Statistical Summary
    with tab3:
        st.dataframe(
            df.describe(),
            use_container_width=True
        )


    # Schema
    with tab4:

        schema_df = pd.DataFrame({
            "Column Name": df.columns,
            "Data Type": [str(x) for x in df.dtypes],
            "Non-Null Count": df.notnull().sum().values,
            "Unique Values": [
                df[column].nunique()
                for column in df.columns
            ]
        })

        st.dataframe(
            schema_df,
            use_container_width=True
        )


    st.markdown("<br><hr>", unsafe_allow_html=True)


    # ---------------- FILTERS ----------------

    st.subheader("🛠️ Quick Tools & Filters")


    with st.expander("🔍 Filter Dataset Live by Airline & Source City"):

        col1, col2 = st.columns(2)


        # Airline options
        airline_options = list(
            df[airline_col].dropna().unique()
        )


        # Source city options
        source_options = list(
            df[source_col].dropna().unique()
        )


        with col1:

            selected_airlines = st.multiselect(
                "Filter Airline:",
                airline_options,
                default=airline_options[:2]
            )


        with col2:

            selected_source = st.multiselect(
                "Filter Source City:",
                source_options,
                default=source_options[:2]
            )


        # Filter data
        filtered_df = df.copy()


        if selected_airlines:
            filtered_df = filtered_df[
                filtered_df[airline_col].isin(selected_airlines)
            ]


        if selected_source:
            filtered_df = filtered_df[
                filtered_df[source_col].isin(selected_source)
            ]


        st.dataframe(
            filtered_df.head(10),
            use_container_width=True
        )


    # ---------------- DOWNLOAD ----------------

    with st.expander("📥 Download Sample or Full Dataset"):

        col1, col2 = st.columns(2)


        with col1:

            st.download_button(
                "Download Sample (100 Rows)",
                df.head(100).to_csv(index=False).encode("utf-8"),
                "sample_flights.csv",
                "text/csv",
                use_container_width=True
            )


        with col2:

            st.download_button(
                "Download Full Dataset",
                df.to_csv(index=False).encode("utf-8"),
                "full_flights.csv",
                "text/csv",
                use_container_width=True
            )

elif opt == "Pre-Processing":

    # Load cleaned dataset
    try:
        df_clean = pd.read_csv("Cleaned_airlines_flight_data.csv")
    except:
        df_clean = df.copy()

    # ---------------- CSS ----------------
    st.markdown(
        """
        <style>

        /* Main Heading */
        .pre-title {
    background: linear-gradient(
        135deg,
        #00f2fe 0%,
        #4facfe 50%,
        #00c6ff 100%
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 2.8rem !important;
    font-weight: 800 !important;
    margin-bottom: 0px;
    text-shadow: 0px 10px 20px rgba(0, 242, 254, 0.2);
}
    
            

        /* Small line below heading */
        .pre-caption {
            color: #a0aec0;
            font-size: 1rem;
            margin-bottom: 18px;
        }

        /* Summary Cards */
        .pre-card {
            background: rgba(22, 45, 73, 0.65);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 14px;
            padding: 18px 10px;
            text-align: center;
            height: 105px;

            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);

            transition: all 0.3s ease;
        }

        /* Hover Effect */
        .pre-card:hover {
            transform: translateY(-6px) scale(1.03);
            border-color: #00eaff;
            box-shadow:
                0 0 12px rgba(0, 234, 255, 0.35),
                0 8px 22px rgba(0, 0, 0, 0.35);
        }

        .pre-card-title {
            color: #a0aec0;
            font-size: 11px;
            font-weight: 700;
            margin-bottom: 6px;
        }

        .pre-card-value {
            font-size: 24px;
            font-weight: 800;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    # ---------------- MAIN HEADING ----------------

    st.markdown(
        """
        <h1 class="pre-title">
            ⚙️ Preprocessed & Cleaned Dataset Overview
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p class="pre-caption">
            Displaying metadata, schema information, missing value verification,
            and structure of the cleaned dataset.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # ---------------- SUMMARY CARDS ----------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            f"""
            <div class="pre-card">
                <div class="pre-card-title">TOTAL CLEAN ROWS</div>
                <div class="pre-card-value" style="color:#00f2fe;">
                    {len(df_clean):,}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="pre-card">
                <div class="pre-card-title">TOTAL COLUMNS</div>
                <div class="pre-card-value" style="color:#00e676;">
                    {df_clean.shape[1]}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <div class="pre-card">
                <div class="pre-card-title">MISSING VALUES</div>
                <div class="pre-card-value" style="color:#ffd700;">
                    {df_clean.isnull().sum().sum()}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            f"""
            <div class="pre-card">
                <div class="pre-card-title">DUPLICATES</div>
                <div class="pre-card-value" style="color:#ff5252;">
                    {df_clean.duplicated().sum()}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------------- DATASET STRUCTURE ----------------

    st.subheader("📋 Dataset Structure & Schema Details")

    tab1, tab2, tab3 = st.tabs(
        [
            "✨ Cleaned Data Preview",
            "⚙️ Data Types & Info",
            "🔍 Missing Values Check"
        ]
    )

    # First Tab
    with tab1:

        st.caption("First 10 rows of your cleaned dataset:")

        st.dataframe(
            df_clean.head(10),
            use_container_width=True
        )

    # Second Tab
    with tab2:

        st.caption("Detailed column summary of cleaned dataset:")

        info_df = pd.DataFrame(
            {
                "Column Name": df_clean.columns,
                "Data Type": [str(dtype) for dtype in df_clean.dtypes],
                "Non-Null Count": df_clean.notnull().sum().values,
                "Unique Values": [
                    df_clean[col].nunique()
                    for col in df_clean.columns
                ],
            }
        )

        st.dataframe(
            info_df,
            use_container_width=True
        )

    # Third Tab
    with tab3:

        null_count = df_clean.isnull().sum().sum()

        if null_count == 0:
            st.success(
                "✅ Excellent! Dataset contains 0 missing values."
            )
        else:
            st.warning(
                f"Found {null_count} missing values."
            )

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------------- DOWNLOAD ----------------

    with st.expander("📥 Download Cleaned Dataset"):

        st.download_button(
            label="Download Cleaned CSV",
            data=df_clean.to_csv(index=False).encode("utf-8"),
            file_name="Cleaned_airlines_flight_data.csv",
            mime="text/csv",
            use_container_width=True
        )

#
elif opt == "Visualization":
    try:
            df_clean=pd.read_csv('Cleaned_airlines_flights_data.csv')
    except Exception:
            df_clean=df.copy()
            



    st.markdown(
        """
        <style>
        .home-title {
            background: linear-gradient(135deg, #00f2fe 0%, #4facfe 50%, #00c6ff 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 2.5rem !important;
            font-weight: 800 !important;
            margin-bottom: 0px;
            text-shadow: 0px 10px 20px rgba(0, 242, 254, 0.2);
        }
        
        .home-caption {
            color: #a0aec0 !important;
            font-size: 1rem !important;
            margin-bottom: 20px;
        }

        .custom-card {
            background: rgba(22, 45, 73, 0.65) !important;
            backdrop-filter: blur(12px) !important;
            -webkit-backdrop-filter: blur(12px) !important;
            border: 1px solid rgba(255, 255, 255, 0.12) !important;
            border-radius: 16px !important;
            padding: 20px !important;
            margin-bottom: 20px !important;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # 
    st.markdown(
        "<h1 class='home-title'>📊 Data Visualization Dashboard</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p class='home-caption'>Explore flight distributions, pricing trends, and detailed analytics.</p>",
        unsafe_allow_html=True,
    )
    st.divider()

    # 3. Tabs
    

    
    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "✈️ Flight Counts",
            "💰 Price Analysis",
            "📅 Timings & Days",
            "🌐 Routes & Heatmaps",
        ]
    )
    
    with tab1:
        st.write("### Airline & Flight Overview")

        # 1. Arrival Time Distribution1
        deep_counts2 = (
            df_clean["Arrival_time"].value_counts(ascending=True).reset_index()
        )
        fig1 = px.bar(
            data_frame=deep_counts2,
            x="Arrival_time",
            y="count",
            title="Arrival Time Destribution",
            labels={
                "Arrival_Time": "Arrival Time",
                "count": "Number of Flights",
            },
            color="Arrival_time",
            template="plotly_white",
            text_auto=True,
            color_discrete_sequence=px.colors.sequential.Blues,
        )
        fig1.update_traces(
            width=0.5,
            marker_line_color="black",
            marker_line_width=1.5,
            textposition="outside",
        )
        st.plotly_chart(fig1, use_container_width=True)

        # 2. Value Counts by Airline
        flight_counts = df_clean["Airline"].value_counts().reset_index()
        flight_counts.columns = ["Airline", "count"]
        fig2 = px.bar(
            flight_counts,
            x="Airline",
            y="count",
            color="Airline",
            title="Value Counts by Airline ",
            text_auto=True,
            color_discrete_sequence=px.colors.sequential.Blues,
            template="plotly_white",
        )
        fig2.update_traces(marker_line_color="Black", marker_line_width=1.5)
        st.plotly_chart(fig2, use_container_width=True)

        # 3. Market Penetration
        Airline_Share = df_clean.groupby("Airline").size().reset_index(name="volume")
        fig3 = px.pie(
            data_frame=Airline_Share,
            names="Airline",
            values="volume",
            title="Market Pentration by Airline",
            color_discrete_sequence=px.colors.sequential.Blues_r,
        )
        fig3.update_layout(showlegend=True)
        st.plotly_chart(fig3, use_container_width=True)

        # 4. Fleet Service Proportions (Stops)
        stops_breakdown = df_clean.groupby("Stops").size().reset_index(name="volume")
        fig4 = px.pie(
            data_frame=stops_breakdown,
            names="Stops",
            values="volume",
            hole=0.5,
            title="Fleet Service Propertions",
            color_discrete_sequence=px.colors.sequential.Blues_r,
        )
        fig4.update_layout(template="plotly_white")
        st.plotly_chart(fig4, use_container_width=True)

        # 5. Capacity Across Strategic Gateways
        source_data = (
            df_clean.groupby("Source_City").size().reset_index(name="Flight_Counts")
        )
        source_data = source_data.sort_values(
            by="Flight_Counts", ascending=True
        )
        fig5 = px.bar(
            data_frame=source_data,
            x="Flight_Counts",
            y="Source_City",
            orientation="h",
            color="Flight_Counts",
            text="Flight_Counts",
            title="Absolute Capacity Across Strategic Gateways",
            template="plotly_white",
            color_continuous_scale="Blues",
        )
        fig5.update_layout(
            xaxis_title="Number of Flights",
            yaxis_title="Source_City",
            font=dict(size=14),
            height=500,
        )
        fig5.update_traces(
            width=0.5,
            marker_line_color="black",
            marker_line_width=1.5,
            textposition="outside",
        )
        st.plotly_chart(fig5, use_container_width=True)

    with tab2:
        st.write("### Ticket Price Trends")

        # 6. Ticket Price Distribution
        fig6 = px.histogram(
            data_frame=df_clean,
            x="Price",
            nbins=30,
            title="Ticket Price Destribution",
            color_discrete_sequence=px.colors.sequential.Viridis,
        )
        fig6.update_layout(bargap=0.1)
        fig6.update_traces(marker_line_color="black", marker_line_width=1.5)
        st.plotly_chart(fig6, use_container_width=True)

        # 7. Benchmark Average Fare Structure
        avg_fare = df_clean.groupby("Airline")["Price"].mean().reset_index()
        fig7 = px.bar(
            data_frame=avg_fare,
            x="Airline",
            y="Price",
            color="Price",
            text_auto=".2f",
            title="Benchmark Average Fare Structure",
            template="plotly_white",
            color_continuous_scale="Blues",
        )
        fig7.update_layout(
            xaxis_title="Airline",
            yaxis_title="Average Ticket Price",
            font=dict(size=14),
            height=500,
        )
        st.plotly_chart(fig7, use_container_width=True)

        # 8. Fare Variance Matrix By Flight Class
        class_fare = (
            df_clean.groupby(["Airline", "Class"])["Price"].mean().reset_index()
        )
        fig8 = px.bar(
            data_frame=class_fare,
            x="Airline",
            y="Price",
            color="Class",
            barmode="group",
            text_auto=".2f",
            title="Fare Variance Matrix By Flight Class",
            template="plotly_white",
            color_discrete_sequence=px.colors.sequential.Blues_r,
        )
        fig8.update_layout(
            xaxis_title="Airline",
            yaxis_title="Average Ticket Price",
            legend_title="Flight Class",
            font=dict(size=14),
            height=500,
        )
        st.plotly_chart(fig8, use_container_width=True)

        # 9. Structural Pricing Density (Sunburst)
        sunburst_data = (
            df_clean.groupby(["Airline", "Destination_City"])["Price"]
            .mean()
            .reset_index()
        )
        fig9 = px.sunburst(
            data_frame=sunburst_data,
            path=["Airline", "Destination_City"],
            values="Price",
            color="Price",
            color_continuous_scale="viridis",
            title="Structural Pricing Density",
        )
        fig9.update_layout(template="plotly_white", height=500)
        st.plotly_chart(fig9, use_container_width=True)

        # 10. Top 10 Most Expensive Flights
        premium_flights = df_clean.groupby("Flight")["Price"].mean().reset_index()
        top_10_premium = premium_flights.sort_values(
            by="Price", ascending=True
        ).head(10)
        fig10 = px.bar(
            data_frame=top_10_premium,
            x="Flight",
            y="Price",
            color="Price",
            text_auto=".2f",
            title="Top 10 Most Expensive Flights",
            template="plotly_white",
            color_continuous_scale="Blues",
        )
        fig10.update_layout(
            xaxis_title="Flight",
            yaxis_title="Average Ticket Price",
            font=dict(size=14),
            height=500,
        )
        fig10.update_xaxes(tickangle=90)
        st.plotly_chart(fig10, use_container_width=True)

    with tab3:
        st.write("### Advance Booking & Timing Windows")

        # 11. Advance Booking Curve
        booking_curve = df_clean.groupby("Days_Left")["Price"].mean().reset_index()
        booking_curve = booking_curve.sort_values(
            by="Days_Left", ascending=True
        )
        fig11 = px.line(
            data_frame=booking_curve,
            x="Days_Left",
            y="Price",
            markers=True,
            title="The Advance Booking Curve",
            template="plotly_white",
        )
        fig11.update_layout(
            xaxis_title="Days Left For Departure",
            yaxis_title="Average Ticket Price",
            font=dict(size=14),
            height=500,
        )
        fig11.update_traces(
            line=dict(color="royalblue", width=3), marker=dict(size=8)
        )
        st.plotly_chart(fig11, use_container_width=True)

        # 12. Split Progression Trajectory
        split_curve = (
            df_clean.groupby(["Days_Left", "Class"])["Price"].mean().reset_index()
        )
        fig12 = px.line(
            data_frame=split_curve,
            x="Days_Left",
            y="Price",
            color="Class",
            markers=True,
            title="Split Progression Trajectory",
            template="plotly_white",
            color_discrete_sequence=px.colors.qualitative.Set2,
        )
        fig12.update_layout(
            xaxis_title="Days Left Before Departure",
            yaxis_title="Average Ticket Price",
            legend_title="Flight Class",
            font=dict(size=14),
            height=500,
        )
        fig12.update_traces(line=dict(width=3), marker=dict(size=7))
        st.plotly_chart(fig12, use_container_width=True)

        # 13. Departure Window Premium Analysis
        fig13 = px.box(
            data_frame=df_clean,
            x="Departure_Time",
            y="Price",
            color="Departure_Time",
            title="Departure Window Premium Analysis",
            template="plotly_white",
            color_discrete_sequence=px.colors.qualitative.Set2,
            points="outliers",
        )
        fig13.update_layout(
            xaxis_title="Departure Time",
            yaxis_title="Ticket Price",
            font=dict(size=14),
            height=500,
            showlegend=False,
        )
        st.plotly_chart(fig13, use_container_width=True)

        # 14. Arrival Window Premium Distribution
        fig14 = px.violin(
            data_frame=df_clean,
            x="Arrival_time",
            y="Price",
            color="Arrival_time",
            box=True,
            points=False,
            title="Arrival Window Premium Distribution",
            template="plotly_white",
            color_discrete_sequence=px.colors.qualitative.Set3,
        )
        fig14.update_layout(
            xaxis_title="Arrival Time",
            yaxis_title="Ticket Price",
            font=dict(size=14),
            height=500,
            showlegend=False,
        )
        st.plotly_chart(fig14, use_container_width=True)

    with tab4:
        st.write("### Route Mapping & Network Heatmaps")

        # 15. Route Proliferation Ranking (Treemap)
        route_hierarchy = (
            df_clean.groupby(["Source_City", "Destination_City"])
            .size()
            .reset_index(name="total_routes")
        )
        fig15 = px.treemap(
            data_frame=route_hierarchy,
            path=["Source_City", "Destination_City"],
            values="total_routes",
            color="total_routes",
            color_continuous_scale="viridis",
            title="Route Proliferatuin Ranking",
        )
        st.plotly_chart(fig15, use_container_width=True)

        # 16. Revenue Density Mapping
        revenue_matrix = (
            df_clean.groupby(["Source_City", "Destination_City"])["Price"]
            .mean()
            .reset_index()
        )
        pivot_table = revenue_matrix.pivot(
            index="Source_City", columns="Destination_City", values="Price"
        )
        fig16 = px.imshow(
            pivot_table,
            text_auto=".0f",
            color_continuous_scale="Blues",
            title="Revenue Density Mapping",
        )
        fig16.update_layout(
            xaxis_title="Destination City",
            yaxis_title="Source City",
            template="plotly_white",
            font=dict(size=14),
            height=500,
        )
        st.plotly_chart(fig16, use_container_width=True)

        # 17. Network Congestion Matrix
        traffic_matrix = (
            df_clean.groupby(["Departure_Time", "Arrival_time"])
            .size()
            .reset_index(name="Flights")
        )
        pivot_traffic = traffic_matrix.pivot(
            index="Departure_Time",
            columns="Arrival_time",
            values="Flights",
        )
        fig17 = px.imshow(
            pivot_traffic,
            text_auto=True,
            color_continuous_scale="Blues",
            title="Network Congestion Matrix",
        )
        fig17.update_layout(
            xaxis_title="Arrival Time",
            yaxis_title="Departure Time",
            template="plotly_white",
            font=dict(size=14),
            height=500,
        )
        fig17.update_xaxes(tickangle=90)
        st.plotly_chart(fig17, use_container_width=True)

        # 18. Operational Duration Elasticity
        visual_sample = df_clean.sample(n=min(2500, len(df)), random_state=42)
        fig18 = px.scatter(
            visual_sample,
            x="Duration",
            y="Price",
            color="Airline",
            opacity=0.5,
            title="Operational Duration Elasticity",
            template="plotly_white",
            color_discrete_sequence=px.colors.qualitative.Set2,
        )
        fig18.update_layout(
            xaxis_title="Flight Duration (Hours)",
            yaxis_title="Ticket Price",
            legend_title="Airline",
            font=dict(size=14),
            height=500,
        )
        st.plotly_chart(fig18, use_container_width=True)

        # 19. Journey Overhead Pricing Structures
        fig19 = px.violin(
            data_frame=df_clean,
            x="Stops",
            y="Price",
            color="Stops",
            box=True,
            points=False,
            title="Journey Overhead Pricing Structures",
            template="plotly_white",
            color_discrete_sequence=px.colors.qualitative.Pastel,
        )
        fig19.update_layout(
            xaxis_title="Number of Stops",
            yaxis_title="Ticket Price",
            font=dict(size=14),
            height=500,
            showlegend=False,
        )
        st.plotly_chart(fig19, use_container_width=True)


elif opt == "About":
    st.markdown(
        """
        <style>
        .home-title {
            background: linear-gradient(135deg, #00f2fe 0%, #4facfe 50%, #00c6ff 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 2.5rem !important;
            font-weight: 800 !important;
            margin-bottom: 0px;
            text-shadow: 0px 10px 20px rgba(0, 242, 254, 0.2);
        }
        
        .home-caption {
            color: #a0aec0 !important;
            font-size: 1rem !important;
            margin-bottom: 20px;
        }

        .custom-card {
            background: rgba(22, 45, 73, 0.65) !important;
            backdrop-filter: blur(12px) !important;
            -webkit-backdrop-filter: blur(12px) !important;
            border: 1px solid rgba(255, 255, 255, 0.12) !important;
            border-radius: 16px !important;
            padding: 22px !important;
            margin-bottom: 20px !important;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        }

        .section-header {
            font-size: 18px;
            font-weight: 700;
            color: #00f2fe;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .badge {
            display: inline-block;
            background: rgba(0, 242, 254, 0.1);
            color: #e2e8f0;
            border: 1px solid rgba(0, 242, 254, 0.3);
            padding: 6px 14px;
            border-radius: 30px;
            font-size: 13px;
            font-weight: 500;
            margin-right: 6px;
            margin-bottom: 8px;
        }
        </style>

        <h1 class="home-title">✈️ Flight Data Analytics Platform</h1>
        <p class="home-caption">An end-to-end interactive dashboard for flight price insights, route analytics, and data cleaning.</p>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    col1, col2 = st.columns([1.2, 1], gap="large")

    with col1:
        st.markdown(
            """
            <div class="custom-card">
                <div class="section-header">📌 Project Purpose</div>
                <p style="color: #cbd5e1; line-height: 1.6;">
                    This dashboard is designed to transform complex raw airline data into clear, actionable visual insights. 
                    It simplifies flight data pre-processing and enables users to explore fare variations and peak travel routes effortlessly.
                </p>
            </div>
            <div class="custom-card">
                <div class="section-header">🚀 Core Capabilities</div>
                <ul style="color: #cbd5e1; line-height: 1.8; padding-left: 20px; margin: 0;">
                    <li><b>Data Cleaning Engine:</b> Automatically detect & handle missing values and export pre-processed datasets.</li>
                    <li><b>Price & Fare Trends:</b> Deep dive into high/low fare ranges, airline pricing variations, and outliers.</li>
                    <li><b>Route & Network Analysis:</b> Visualize top departure hubs, busiest routes, and heatmap patterns.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="custom-card">
                <div class="section-header">🛠️ Tech Stack</div>
                <div style="margin-top: 10px;">
                    <span class="badge">🐍 Python 3.x</span>
                    <span class="badge">🚀 Streamlit</span>
                    <span class="badge">📊 Pandas & NumPy</span>
                    <span class="badge">📈 Plotly Express</span>
                    <span class="badge">🎨 CSS3 Layouts</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        with st.expander("ℹ️ How to navigate this app?"):
            st.write(
                """
            1. **Data Overview:** View raw dataset & basic summary statistics.
            2. **Pre-processing:** Clean missing values and download clean CSV.
            3. **Visualization:** Explore interactive charts across different tabs.
            """
            )

    st.divider()

    st.caption(
        "⚡ *Built for Data Analytics & Interactive Visualization Project*"
    )
