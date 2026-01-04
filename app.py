import streamlit as st
import pickle
import pandas as pd
import numpy as np
import math

# Config
st.set_page_config(page_title="CAN 2025 Predictor", page_icon="⚽", layout="wide")

# Fallback: country codes
FLAG_CODES = {
    'Morocco': 'MA', 'Mali': 'ML', 'Zambia': 'ZM', 'Comoros': 'KM',
    'Egypt': 'EG', 'South Africa': 'ZA', 'Angola': 'AO', 'Zimbabwe': 'ZW',
    'Nigeria': 'NG', 'Tunisia': 'TN', 'Uganda': 'UG', 'Tanzania': 'TZ',
    'Senegal': 'SN', 'DR Congo': 'CD', 'Benin': 'BJ', 'Botswana': 'BW',
    'Algeria': 'DZ', 'Burkina Faso': 'BF', 'Equatorial Guinea': 'GQ', 'Sudan': 'SD',
    'Ivory Coast': 'CI', 'Cameroon': 'CM', 'Gabon': 'GA', 'Mozambique': 'MZ'
}

def get_flag(team):
    code = FLAG_CODES.get(team, 'XX')
    return f'<img src="https://flagcdn.com/16x12/{code.lower()}.png" width="20">'

# Charger les modèles
@st.cache_resource
def load_models():
    with open('model_home.pkl', 'rb') as f:
        model_home = pickle.load(f)
    with open('model_away.pkl', 'rb') as f:
        model_away = pickle.load(f)
    with open('teams_data.pkl', 'rb') as f:
        teams_data = pickle.load(f)
    with open('groups.pkl', 'rb') as f:
        groups = pickle.load(f)
    return model_home, model_away, teams_data, groups

model_home, model_away, teams_data, groups = load_models()

# Fix Zambia ranking
if 'Zambia' in teams_data:
    teams_data['Zambia']['rank'] = 91

# Distance function
capitals = {
    'Morocco': (34.0209, -6.8416), 'Mali': (12.6392, -8.0029), 'Zambia': (-15.3875, 28.3228),
    'Comoros': (-11.7172, 43.2473), 'Egypt': (30.0444, 31.2357), 'South Africa': (-25.7479, 28.2293),
    'Angola': (-8.8147, 13.2302), 'Zimbabwe': (-17.8216, 31.0492), 'Nigeria': (9.0765, 7.3986),
    'Tunisia': (36.8065, 10.1815), 'Uganda': (0.3476, 32.5825), 'Tanzania': (-6.1630, 35.7516),
    'Senegal': (14.7167, -17.4677), 'DR Congo': (-4.4419, 15.2663), 'Benin': (6.4969, 2.6289),
    'Botswana': (-24.6282, 25.9231), 'Algeria': (36.7528, 3.0420), 'Burkina Faso': (12.3714, -1.5197),
    'Equatorial Guinea': (3.7504, 8.7371), 'Sudan': (15.5007, 32.5599), 'Ivory Coast': (6.8276, -5.2500),
    'Cameroon': (3.8480, 11.5021), 'Gabon': (0.4162, 9.4673), 'Mozambique': (-25.9692, 32.5732)
}

def get_distance_rabat(team_name):
    if team_name not in capitals:
        return 2000
    lat1, lon1 = capitals['Morocco']
    lat2, lon2 = capitals[team_name]
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

# Predict function
def predict_match(team1, team2):
    t1 = teams_data.get(team1)
    t2 = teams_data.get(team2)
    
    r_diff = t1.get('rank', 50) - t2.get('rank', 50)
    p_diff = t1.get('points', 1000) - t2.get('points', 1000)
    mv_diff = t1.get('market_value', 0) - t2.get('market_value', 0)
    
    X_input = pd.DataFrame([[
        r_diff, p_diff, mv_diff,
        t1.get('momentum', 0), t2.get('momentum', 0),
        t1.get('att_form', 1.0), t2.get('att_form', 1.0),
        t1.get('def_form', 1.0), t2.get('def_form', 1.0),
        0
    ]], columns=['rank_diff', 'points_diff', 'market_value_diff',
                 'home_momentum', 'away_momentum',
                 'home_attack_form', 'away_attack_form',
                 'home_defense_form', 'away_defense_form', 'is_friendly'])
    
    exp_goals_t1 = model_home.predict(X_input)[0]
    exp_goals_t2 = model_away.predict(X_input)[0]
    
    # Adjustments
    d1, d2 = get_distance_rabat(team1), get_distance_rabat(team2)
    exp_goals_t1 -= (d1 / 1000) * 0.05
    exp_goals_t2 -= (d2 / 1000) * 0.05
    
    if t1.get('is_host'): exp_goals_t1 += 0.4
    if t2.get('is_host'): exp_goals_t2 += 0.4
    
    s1 = np.random.poisson(max(0.05, exp_goals_t1))
    s2 = np.random.poisson(max(0.05, exp_goals_t2))
    
    return s1, s2, exp_goals_t1, exp_goals_t2

# UI
st.title("⚽ CAN 2025 Predictor")
st.markdown("Prédis le résultat de n'importe quel match de la Coupe d'Afrique")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["🎯 Match Unique", "🏆 Groupes", "🎲 Simulation Unique", "📊 Monte Carlo", "📈 Stats Équipes"])

# Tab 1: Match prediction
with tab1:
    col1, col2 = st.columns(2)
    
    all_teams = list(teams_data.keys())
    
    with col1:
        team1 = st.selectbox("Équipe 1", all_teams, key="t1")
        
    with col2:
        team2 = st.selectbox("Équipe 2", all_teams, key="t2")
    
    if st.button("🔮 Prédire", type="primary"):
        if team1 == team2:
            st.error("Choisis deux équipes différentes!")
        else:
            with st.spinner("Calcul en cours..."):
                results = []
                for _ in range(100):
                    s1, s2, _, _ = predict_match(team1, team2)
                    results.append((s1, s2))
                
                # Stats
                t1_wins = sum(1 for s1, s2 in results if s1 > s2)
                draws = sum(1 for s1, s2 in results if s1 == s2)
                t2_wins = sum(1 for s1, s2 in results if s1 < s2)
                
                avg_s1 = np.mean([s1 for s1, s2 in results])
                avg_s2 = np.mean([s2 for s1, s2 in results])
                
                st.markdown("---")
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric(f"🏆 {team1} gagne", f"{t1_wins}%")
                with col2:
                    st.metric("🤝 Match Nul", f"{draws}%")
                with col3:
                    st.metric(f"🏆 {team2} gagne", f"{t2_wins}%")
                
                st.markdown("---")
                
                st.subheader("📊 Score Prédit")
                col1, col2, col3 = st.columns([2,1,2])
                
                with col1:
                    st.markdown(f"<h1 style='text-align: center;'>{get_flag(team1)} {team1}</h1>", unsafe_allow_html=True)
                with col2:
                    st.markdown(f"<h1 style='text-align: center; color: #ff4b4b;'>{avg_s1:.1f} - {avg_s2:.1f}</h1>", unsafe_allow_html=True)
                with col3:
                    st.markdown(f"<h1 style='text-align: center;'>{team2} {get_flag(team2)}</h1>", unsafe_allow_html=True)

# Tab 2: Groups
with tab2:
    st.subheader("🏆 Groupes CAN 2025")
    
    cols = st.columns(3)
    group_names = list(groups.keys())
    
    for idx, (grp, teams) in enumerate(groups.items()):
        with cols[idx % 3]:
            st.markdown(f"### Groupe {grp}")
            for team in teams:
                rank = teams_data[team].get('rank', 0)
                rank_display = int(rank) if rank > 0 else 'N/A'
                st.markdown(f"{get_flag(team)} **{team}** (FIFA: {rank_display})", unsafe_allow_html=True)
            st.markdown("---")

# Tab 3: Single simulation
with tab3:
    st.subheader("🎲 Simulation Complète de la CAN")
    
    if st.button("🚀 Simuler le Tournoi", type="primary", key="single_sim"):
        
        results_log = []
        
        with st.spinner("Phase de groupes..."):
            st.markdown("### 📋 PHASE DE GROUPES")
            
            standings = {}
            thirds = []
            
            for grp_name, teams in groups.items():
                st.markdown(f"#### Groupe {grp_name}")
                pts = {t: 0 for t in teams}
                gf = {t: 0 for t in teams}
                gd = {t: 0 for t in teams}
                
                for i in range(len(teams)):
                    for j in range(i+1, len(teams)):
                        s1, s2, _, _ = predict_match(teams[i], teams[j])
                        
                        if s1 > s2: pts[teams[i]] += 3
                        elif s2 > s1: pts[teams[j]] += 3
                        else: pts[teams[i]]+=1; pts[teams[j]]+=1
                        
                        gd[teams[i]]+=(s1-s2); gd[teams[j]]+=(s2-s1)
                        gf[teams[i]]+=s1; gf[teams[j]]+=s2
                        
                        st.markdown(f"{get_flag(teams[i])} {teams[i]} {s1}-{s2} {teams[j]} {get_flag(teams[j])}", unsafe_allow_html=True)
                
                ranking = sorted(teams, key=lambda x: (pts[x], gd[x], gf[x]), reverse=True)
                standings[grp_name] = {'1': ranking[0], '2': ranking[1], '3': ranking[2]}
                thirds.append({'t': ranking[2], 'g': grp_name, 'p': pts[ranking[2]], 'd': gd[ranking[2]], 'f': gf[ranking[2]]})
                
                st.success(f"Qualifiés: {ranking[0]}, {ranking[1]}")
                st.markdown("---")
        
        best3 = sorted(thirds, key=lambda x: (x['p'], x['d'], x['f']), reverse=True)[:4]
        st.info(f"Meilleurs 3èmes: {', '.join([t['t'] for t in best3])}")
        
        st.markdown("### 🔥 HUITIÈMES DE FINALE")
        
        def play_knockout(t1, t2, stage_name):
            s1, s2, _, _ = predict_match(t1, t2)
            if s1 == s2:
                winner = t1 if np.random.rand() > 0.5 else t2
                st.markdown(f"{get_flag(t1)} {t1} **{s1}-{s2}** {t2} {get_flag(t2)} → **{winner}** (TAB)", unsafe_allow_html=True)
            else:
                winner = t1 if s1 > s2 else t2
                st.markdown(f"{get_flag(t1)} {t1} **{s1}-{s2}** {t2} {get_flag(t2)} → ✅ **{winner}**", unsafe_allow_html=True)
            return winner
        
        r16 = [
            (standings['A']['1'], best3[0]['t']),
            (standings['B']['1'], best3[1]['t']),
            (standings['C']['1'], best3[2]['t']),
            (standings['D']['1'], best3[3]['t']),
            (standings['E']['1'], standings['F']['2']),
            (standings['F']['1'], standings['E']['2']),
            (standings['A']['2'], standings['C']['2']),
            (standings['B']['2'], standings['D']['2'])
        ]
        
        winners_r16 = [play_knockout(t1, t2, "R16") for t1, t2 in r16]
        
        st.markdown("### ⚔️ QUARTS DE FINALE")
        qf = [(winners_r16[i], winners_r16[i+1]) for i in range(0, 8, 2)]
        winners_qf = [play_knockout(t1, t2, "QF") for t1, t2 in qf]
        
        st.markdown("### 🏆 DEMI-FINALES")
        sf = [(winners_qf[0], winners_qf[1]), (winners_qf[2], winners_qf[3])]
        winners_sf = [play_knockout(t1, t2, "SF") for t1, t2 in sf]
        
        st.markdown("### 🥇 FINALE")
        champion = play_knockout(winners_sf[0], winners_sf[1], "Final")
        
        st.balloons()
        st.markdown(f"## 🎉 CHAMPION: **{champion.upper()}** 🏆")

# Tab 4: Monte Carlo
with tab4:
    st.subheader("📊 Simulation Monte Carlo")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        n_sims = st.slider("Nombre de simulations", 100, 10000, 1000, step=100)
    
    with col2:
        st.info("Plus de simulations = résultats plus précis (mais plus lent)")
    
    if st.button("🚀 Lancer la simulation", type="primary"):
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        knockout_stats = {team: {'R16': 0, 'QF': 0, 'SF': 0, 'Final': 0, 'Winner': 0} for team in teams_data.keys()}
        
        def simulate_group_stage():
            standings = {}
            thirds = []
            
            for grp_name, teams in groups.items():
                pts = {t: 0 for t in teams}
                gf = {t: 0 for t in teams}
                gd = {t: 0 for t in teams}
                
                for i in range(len(teams)):
                    for j in range(i+1, len(teams)):
                        s1, s2, _, _ = predict_match(teams[i], teams[j])
                        
                        if s1 > s2: pts[teams[i]] += 3
                        elif s2 > s1: pts[teams[j]] += 3
                        else: pts[teams[i]]+=1; pts[teams[j]]+=1
                        
                        gd[teams[i]]+=(s1-s2); gd[teams[j]]+=(s2-s1)
                        gf[teams[i]]+=s1; gf[teams[j]]+=s2
                
                ranking = sorted(teams, key=lambda x: (pts[x], gd[x], gf[x]), reverse=True)
                standings[grp_name] = {'1': ranking[0], '2': ranking[1], '3': ranking[2]}
                thirds.append({'t': ranking[2], 'g': grp_name, 'p': pts[ranking[2]], 'd': gd[ranking[2]], 'f': gf[ranking[2]]})
            
            return standings, thirds
        
        def simulate_knockout(standings, thirds):
            best3 = sorted(thirds, key=lambda x: (x['p'], x['d'], x['f']), reverse=True)[:4]
            
            def get3(idx):
                return best3[idx]['t'] if idx < len(best3) else list(teams_data.keys())[0]
            
            # R16
            r16 = [
                (standings['A']['1'], get3(0)),
                (standings['B']['1'], get3(1)),
                (standings['C']['1'], get3(2)),
                (standings['D']['1'], get3(3)),
                (standings['E']['1'], standings['F']['2']),
                (standings['F']['1'], standings['E']['2']),
                (standings['A']['2'], standings['C']['2']),
                (standings['B']['2'], standings['D']['2'])
            ]
            
            winners_r16 = []
            for t1, t2 in r16:
                s1, s2, _, _ = predict_match(t1, t2)
                winner = t1 if s1 > s2 else (t2 if s2 > s1 else (t1 if np.random.rand() > 0.5 else t2))
                winners_r16.append(winner)
                knockout_stats[winner]['QF'] += 1
            
            # QF
            qf = [(winners_r16[i], winners_r16[i+1]) for i in range(0, 8, 2)]
            winners_qf = []
            for t1, t2 in qf:
                s1, s2, _, _ = predict_match(t1, t2)
                winner = t1 if s1 > s2 else (t2 if s2 > s1 else (t1 if np.random.rand() > 0.5 else t2))
                winners_qf.append(winner)
                knockout_stats[winner]['SF'] += 1
            
            # SF
            sf = [(winners_qf[0], winners_qf[1]), (winners_qf[2], winners_qf[3])]
            winners_sf = []
            for t1, t2 in sf:
                s1, s2, _, _ = predict_match(t1, t2)
                winner = t1 if s1 > s2 else (t2 if s2 > s1 else (t1 if np.random.rand() > 0.5 else t2))
                winners_sf.append(winner)
                knockout_stats[winner]['Final'] += 1
            
            # Final
            s1, s2, _, _ = predict_match(winners_sf[0], winners_sf[1])
            champion = winners_sf[0] if s1 > s2 else (winners_sf[1] if s2 > s1 else (winners_sf[0] if np.random.rand() > 0.5 else winners_sf[1]))
            knockout_stats[champion]['Winner'] += 1
            
            return champion
        
        # Run simulations
        for i in range(n_sims):
            standings, thirds = simulate_group_stage()
            
            for grp_name, teams_dict in standings.items():
                knockout_stats[teams_dict['1']]['R16'] += 1
                knockout_stats[teams_dict['2']]['R16'] += 1
            
            for third in sorted(thirds, key=lambda x: (x['p'], x['d'], x['f']), reverse=True)[:4]:
                knockout_stats[third['t']]['R16'] += 1
            
            simulate_knockout(standings, thirds)
            
            progress_bar.progress((i + 1) / n_sims)
            if i % 100 == 0:
                status_text.text(f"Simulation {i+1}/{n_sims}...")
        
        status_text.text("✅ Simulation terminée!")
        progress_bar.empty()
        
        # Results
        st.markdown("---")
        st.subheader("🏆 Probabilités de Victoire")
        
        results_df = pd.DataFrame([
            {
                'Équipe': team,
                'Champion (%)': (stats['Winner'] / n_sims) * 100,
                'Finale (%)': (stats['Final'] / n_sims) * 100,
                'Demi (%)': (stats['SF'] / n_sims) * 100,
                'Quart (%)': (stats['QF'] / n_sims) * 100
            }
            for team, stats in knockout_stats.items()
        ]).sort_values('Champion (%)', ascending=False).head(10)
        
        st.dataframe(results_df.style.format({
            'Champion (%)': '{:.2f}',
            'Finale (%)': '{:.2f}',
            'Demi (%)': '{:.2f}',
            'Quart (%)': '{:.2f}'
        }), use_container_width=True)
        
        st.markdown("---")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("🥇 Favori", results_df.iloc[0]['Équipe'], f"{results_df.iloc[0]['Champion (%)']:.1f}%")
        with col2:
            st.metric("🥈 Outsider", results_df.iloc[1]['Équipe'], f"{results_df.iloc[1]['Champion (%)']:.1f}%")
        with col3:
            st.metric("🥉 Surprise", results_df.iloc[2]['Équipe'], f"{results_df.iloc[2]['Champion (%)']:.1f}%")

# Tab 5: Team stats
with tab5:
    st.subheader("📈 Statistiques des Équipes")
    
    selected_team = st.selectbox("Choisis une équipe", all_teams)
    
    if selected_team:
        data = teams_data[selected_team]
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            rank = data.get('rank', 0)
            rank_display = int(rank) if rank > 0 else 'N/A'
            st.metric("🏅 Rang FIFA", rank_display)
        with col2:
            points = data.get('points', 0)
            points_display = int(points) if points > 0 else 'N/A'
            st.metric("⚡ Points FIFA", points_display)
        with col3:
            st.metric("💰 Valeur (M€)", f"{data.get('market_value', 0):.1f}")
        with col4:
            momentum = data.get('momentum', 0)
            st.metric("📈 Momentum", f"{momentum:+.0f}", delta=f"{momentum:+.0f}")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 🎯 Forme Offensive")
            att = data.get('att_form', 0)
            st.progress(min(att / 3, 1.0))
            st.write(f"**{att:.2f}** buts/match (5 derniers)")
            
        with col2:
            st.markdown("### 🛡️ Forme Défensive")
            deff = data.get('def_form', 0)
            st.progress(min(deff / 3, 1.0))
            st.write(f"**{deff:.2f}** buts encaissés/match")

st.markdown("---")
st.caption("Modèle: Random Forest | MAE: 0.842 | Accuracy: 54.49%")