class MultimodalAspectRatioSmartReframeClient:
    def calculate_smart_reframe(self, source_aspect_ratio='16:9', target_aspect_ratio='9:16', active_speaker_coordinates={'x_pct': 48.5, 'y_pct': 35.0, 'width_pct': 22.0, 'height_pct': 40.0}):
        return {
            'reframe_plan_id': 'rfm_pln_4412',
            'source_ratio': source_aspect_ratio,
            'target_ratio': target_aspect_ratio,
            'crop_viewport': {'center_x_pct': 48.5, 'crop_width_pct': 56.25, 'crop_height_pct': 100.0},
            'speaker_centered': True,
            'smooth_pan_interpolation': 'CUBIC_BEZIER_EASE_IN_OUT',
            'motion_tracking_confidence': 0.98,
            'reframe_script_url': 'https://media.video.genpark.ai/reframe/rfm_pln_4412.json'
        }
