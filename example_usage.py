from client import MultimodalAspectRatioSmartReframeClient

def main():
    client = MultimodalAspectRatioSmartReframeClient()
    res = client.calculate_smart_reframe()
    print('Smart Reframe Planner: ' + res['reframe_plan_id'] + ' (' + res['source_ratio'] + ' -> ' + res['target_ratio'] + ')')
    print('Speaker Centered: ' + str(res['speaker_centered']) + ' | Confidence: ' + str(res['motion_tracking_confidence']))
    print('Script URL: ' + res['reframe_script_url'])

if __name__ == '__main__':
    main()
