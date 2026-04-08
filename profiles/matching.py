def find_matches(user, all_profiles):
    user_profile = user.profile
    user_interests = set(user_profile.get_interests_list())
    
    matches = []
    for profile in all_profiles:
        if profile.user == user or not profile.is_active:
            continue
        
        profile_interests = set(profile.get_interests_list())
        if user_interests and profile_interests:
            common = len(user_interests & profile_interests)
            total = len(user_interests | profile_interests)
            score = (common / total) * 100 if total > 0 else 0
        else:
            score = 0
        
        matches.append({
            'user': profile.user,
            'profile': profile,
            'score': round(score, 1),
        })
    
    return sorted(matches, key=lambda x: x['score'], reverse=True)[:20]
